"""
RAG Pipeline - LangChain + OpenAI + Qdrant

Uses LangChain to build a retrieval-augmented generation chain backed by
Qdrant (CWICR construction cost data) and OpenAI for both embeddings and
chat completion.
"""

import argparse
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from qdrant_client import QdrantClient

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIMS = 3072
DEFAULT_COLLECTION = "ddc_en_toronto"
DEFAULT_TOP_K = 10
OPENAI_CHAT_MODEL = "gpt-4o"

EXAMPLE_QUERIES = [
    "What is the cost of reinforced concrete foundation work?",
    "List the most expensive excavation items with their rate codes.",
    "What are typical labour hours for interior plastering?",
    "Which departments have the highest material costs?",
]

PROMPT_TEMPLATE = """\
You are a construction cost estimation assistant. Use ONLY the following
CWICR (Construction Work Items, Costs & Resources) data to answer the
question. If the data does not contain enough information, say so.
Always cite rate codes when referencing specific work items. Present costs
in EUR unless asked otherwise.

Context:
{context}

Question: {question}

Answer:
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_qdrant_client() -> QdrantClient:
    url = os.getenv("QDRANT_URL", "http://localhost:6333")
    api_key = os.getenv("QDRANT_API_KEY")
    return QdrantClient(url=url, api_key=api_key)


def build_retriever(
    collection: str,
    top_k: int,
):
    """Build a LangChain retriever backed by an existing Qdrant collection."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set in .env or environment.")

    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        openai_api_key=api_key,
    )

    qdrant_client = get_qdrant_client()

    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection,
        embedding=embeddings,
    )

    return vector_store.as_retriever(search_kwargs={"k": top_k})


def build_chain(retriever, chat_model: str = OPENAI_CHAT_MODEL):
    """Create a RetrievalQA chain with a custom prompt."""
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )

    llm = ChatOpenAI(
        model=chat_model,
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    return chain


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="LangChain RAG pipeline over CWICR data (Qdrant + OpenAI).",
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        default=EXAMPLE_QUERIES[0],
        help="Natural-language question about construction costs.",
    )
    parser.add_argument(
        "--collection", "-c",
        type=str,
        default=DEFAULT_COLLECTION,
        help=f"Qdrant collection name (default: {DEFAULT_COLLECTION}).",
    )
    parser.add_argument(
        "--top-k", "-k",
        type=int,
        default=DEFAULT_TOP_K,
        help=f"Number of results to retrieve (default: {DEFAULT_TOP_K}).",
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default=OPENAI_CHAT_MODEL,
        help=f"OpenAI chat model (default: {OPENAI_CHAT_MODEL}).",
    )
    parser.add_argument(
        "--show-sources",
        action="store_true",
        help="Print retrieved source documents.",
    )
    args = parser.parse_args()

    print(f"\n{'='*70}")
    print(f"Query: {args.query}")
    print(f"Collection: {args.collection}  |  top_k: {args.top_k}  |  model: {args.model}")
    print(f"{'='*70}\n")

    # --- Build chain ---
    print("[1/2] Building retrieval chain ...")
    retriever = build_retriever(args.collection, args.top_k)
    chain = build_chain(retriever, chat_model=args.model)

    # --- Run query ---
    print("[2/2] Running query ...")
    result = chain.invoke({"query": args.query})

    answer = result["result"]
    sources = result.get("source_documents", [])

    print(f"\n{'='*70}")
    print("ANSWER")
    print(f"{'='*70}\n")
    print(answer)

    if args.show_sources and sources:
        print(f"\n{'='*70}")
        print(f"SOURCE DOCUMENTS ({len(sources)})")
        print(f"{'='*70}\n")
        for i, doc in enumerate(sources, 1):
            print(f"--- Source {i} ---")
            metadata = doc.metadata or {}
            for key in ("rate_code", "rate_final_name", "rate_unit",
                        "total_cost_per_position", "department_name"):
                val = metadata.get(key)
                if val is not None:
                    print(f"  {key}: {val}")
            content_preview = (doc.page_content[:200] + "...") if len(doc.page_content) > 200 else doc.page_content
            print(f"  content: {content_preview}")
            print()

    print()


if __name__ == "__main__":
    main()
