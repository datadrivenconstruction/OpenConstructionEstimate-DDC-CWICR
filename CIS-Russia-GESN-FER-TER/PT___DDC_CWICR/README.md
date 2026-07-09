# OpenConstructionEstimate

**Construction Work Items, Components & Resources**

---

**Formatos disponíveis**

| Format | Description |
|--------|-------------|
| Excel (.xlsx) | Formato universal para análise de dados |
| Parquet (.parquet) | Formato colunar para Big Data e ML |
| CSV (.csv) | Formato de texto universal |

---

## Sobre a base de dados

A indústria moderna da construção na Eurásia e na região Ásia-Pacífico baseia-se num ecossistema unificado de padronização técnica que serve como linguagem de engenharia comum para mais de 10 economias em desenvolvimento dinâmico.

A base de dados DDC CWICR (Construction Work Items, Components & Resources) é uma tentativa de harmonizar padrões, criando um espaço regulatório contínuo para a gestão de projetos de capital em vários idiomas. A base de dados abrange todo o espectro de trabalhos de construção: desde terraplanagem e betão até operações de instalação especializadas.

## Fontes de dados

O DDC CWICR é construído com base em padrões oficiais de custos de construção de países eurasiáticos que estão disponíveis publicamente. A base de dados foi desenvolvida em estreita colaboração com orçamentistas e especialistas em construção de diferentes países, o que nos permitiu levar em conta aspectos práticos do trabalho com dados. Os dados foram sistematizados numa estrutura unificada, harmonizados metodologicamente e apresentados em 11 versões linguísticas e 11 versões de preços regionais para uso internacional.

## Desenvolvimento histórico

A metodologia de padronização baseada em recursos dos trabalhos de construção tem se desenvolvido e melhorado continuamente desde a década de 1920 - das primeiras normas de produção aos livros de referência digitais modernos. Ao longo de um século, o sistema evoluiu de cálculos manuais para bases de dados legíveis por máquina, preservando o princípio fundamental: o registo preciso de recursos físicos por unidade de produção de construção.

A versão moderna integra dados históricos com preços de mercado atuais. Nos mercados locais, sistemas semelhantes são adaptados e conhecidos sob códigos nacionais: ENIR, GESN, FER, NRR, ESN, AzDTN, ShNQK, MKS ChT, SNT, BNbD, Dinh Muc, Ding'e.

## Metodologia Resource-Based Costing

O valor-chave do Resource-Based Costing é a separação da tecnologia de produção imutável do componente financeiro volátil: baseia-se nos "primeiros princípios" físicos da construção - normas padrão para custos de mão de obra, tempo de máquina e consumo de materiais. Estas normas permanecem praticamente inalteradas independentemente do país onde a construção é realizada.

Isso permite preços transparentes, elimina margens ocultas e permite uma auditoria profunda (Deep-Dive Audit) de investimentos. Como resultado, o DDC CWICR serve não apenas como um livro de referência, mas como uma ferramenta fundamental de gestão de riscos que se tornou o padrão de facto da indústria para a macro-região ao longo do último século.

## Estatísticas da base de dados

- **55.719** itens de trabalho e tarifas
- **27.672** recursos únicos
- **10+** países de aplicação


## Estrutura de dados

A base de dados contém 85 colunas organizadas em grupos lógicos:

### Hierarquia de classificação
*10 colunas*

category_type, collection_code/name, department_code/name, section_name, subsection_code/name

### Tarifa (Work Item)
*11 colunas*

rate_code, rate_original_name, rate_unit, row_type, flags is_material/is_labor/is_machine/is_abstract

### Recursos
*7 colunas*

resource_code, resource_name, resource_unit, resource_quantity, resource_price_per_unit, resource_cost

### Mão de obra
*11 colunas*

count_workers/engineers/operators, labor_hours por categoria, cost_of_working_hours

### Máquinas e equipamentos
*12 colunas*

machine_class, personnel_operator_grade, electricity_consumption_kwh, electricity_cost

### Variantes de preço
*16 colunas*

price_est_min/max/median/mean, position_count, tech_group

### Massa
*3 colunas*

mass_name, mass_value, mass_unit

## Casos de uso

- **Benchmarking de custos** - Comparar custos entre regiões
- **Indexação de preços** - Acompanhar dinâmicas
- **Localização** - Adaptar às condições locais
- **Pipelines ETL/BI** - Extrair e transformar dados
- **Treino IA/ML** - Treinar modelos
- **Integração CAD (BIM) 5D** - Atribuição automática de tarifas
- **Estimativa de concursos** - Estimativas rápidas
- **Cálculo de CO2** - Calcular pegada de carbono
- **Auditoria profunda** - Auditoria técnica


## Cobertura geográfica

A metodologia e a base de dados são aplicadas em várias adaptações nas seguintes regiões:

- **Eurásia Central (CEI)**: Bielorrússia, Cazaquistão, Quirguistão, Rússia, Tajiquistão, Turquemenistão, Uzbequistão
- **Cáucaso**: Arménia, Azerbaijão, Geórgia
- **Europa Oriental**: Moldávia, Ucrânia
- **Ásia Oriental (Sistema de cotas)**: China (Ding'e), Mongólia (BNbD), Vietname (Dinh Muc)
- **Projetos internacionais**: Bangladesh, Egito, Turquia
- **Aplicação histórica (1950-1990)**: Bulgária, Checoslováquia, Hungria


## Colaboração e desenvolvimento

Estamos abertos ao diálogo com a comunidade profissional. A sua experiência no uso da base de dados em projetos reais ajuda a melhorar a plataforma e expandir as suas capacidades. Partilhe casos de uso, sugira melhorias e participe em discussões.

- **GitHub**: [github.com/datadrivenconstruction](https://github.com/datadrivenconstruction)
- **Telegram**: [t.me/datadrivenconstruction](https://t.me/datadrivenconstruction)
- **LinkedIn**: [linkedin.com/company/datadrivenconstruction](https://linkedin.com/company/datadrivenconstruction)


## Consultoria e formação

Trabalhamos com agências líderes de construção, engenharia, consultoria e empresas de tecnologia em todo o mundo para ajudá-las a implementar princípios de dados abertos, automatizar o processamento CAD/BIM e construir pipelines ETL robustos.

Se deseja testar esta solução com os seus próprios dados, ou está interessado em adaptar o fluxo de trabalho a tarefas de projetos reais, não hesite em contactar-nos. A nossa equipa oferece workshops práticos, fornece consultoria estratégica e desenvolve protótipos adaptados a processos de projetos reais.

Apoiamos ativamente organizações que procuram soluções práticas para transformação digital e interoperabilidade, focando em desafios de qualidade de dados e classificação, e impulsionando a adoção de fluxos de trabalho abertos e automatizados.

Contacte-nos para uma consulta gratuita onde discutiremos os seus desafios e demonstraremos como a automação n8n pode transformar as suas operações. Entre em contacto por e-mail em info@datadrivenconstruction.io ou visite o nosso website datadrivenconstruction.io para saber mais sobre os nossos serviços.



## Apoie o projeto

Se acha as nossas ferramentas e bases de dados úteis e gostaria de ver mais aplicações para a indústria da construção, por favor dê uma estrela aos nossos repositórios no GitHub. Isso ajuda o projeto a crescer e permite-lhe receber notificações sobre novos lançamentos.

Com base no DDC CWICR, pode construir pipelines e fluxos de trabalho automatizados para integração com CAD (BIM), sistemas de concursos e plataformas BI. Novos fluxos de trabalho, ferramentas e soluções prontas são publicados regularmente no GitHub e no website do projeto. Subscreva as atualizações para ser o primeiro a aceder a novos lançamentos.

- ⭐ **CAD (BIM) Data Agents & Workflows + AI**: [github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)
- ⭐ **OpenConstructionEstimate DDC CWICR**: [github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR)


## Versões linguísticas

A documentação está disponível em 11 idiomas:

- **Árabe / العربية** (Dubai) - Médio Oriente
- **Chinês / 中文** (Xangai) - Ásia Oriental
- **Alemão / Deutsch** (Berlim) - Europa Central
- **Inglês / English** (Toronto) - América do Norte
- **Espanhol / Español** (Barcelona) - Ibéria
- **Francês / Français** (Paris) - Europa Ocidental
- **Hindi / हिन्दी** (Mumbai) - Ásia do Sul
- **Português** (São Paulo) - América Latina
- **Russo / Русский** (São Petersburgo) - CEI


## Recursos

- **Exemplo de uso:** https://openconstructionestimate.com
- **Website:** https://datadrivenconstruction.io


---

### Liberte o poder dos dados na construção 🚀

Passe para a gestão de dados de ciclo completo onde apenas dados estruturados unificados e processos permanecem e onde 🔓 os seus dados são seus

---

*[Artem Boiko, 2025](https://www.linkedin.com/in/boikoartem/)*
