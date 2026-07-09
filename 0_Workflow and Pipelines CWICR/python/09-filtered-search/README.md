# 09 - Filtered Search

Advanced Qdrant search examples that combine vector similarity search with payload filters for precise, faceted queries over CWICR data.

## Scripts

| Script | Description |
|---|---|
| `advanced_search.py` | Demonstrates multiple filter combinations: department, price range, unit type, and more |

## Filter Examples

- **Department filter** - find items in a specific department (e.g., "Concrete", "Electrical")
- **Price range** - find items within a cost range (e.g., 100-500 EUR)
- **Unit type** - filter by measurement unit (e.g., m3, m2, kg)
- **Combined filters** - department + price range + material flag
- **Boolean filters** - items flagged as material, machine, or abstract

## Prerequisites

```bash
pip install openai qdrant-client python-dotenv tabulate
```

Create a `.env` file:

```
OPENAI_API_KEY=sk-...
QDRANT_URL=https://your-qdrant-instance.cloud
QDRANT_API_KEY=your-qdrant-api-key
```

## Usage

```bash
# Run all filter examples
python advanced_search.py

# Search with a specific query and department filter
python advanced_search.py --query "foundation waterproofing" --department "Concrete"

# Filter by price range
python advanced_search.py --query "insulation" --min-cost 50 --max-cost 500

# Filter by unit type
python advanced_search.py --query "steel reinforcement" --unit "kg"
```
