# OpenConstructionEstimate

**Construction Work Items, Components & Resources**

---

**Available Formats**

| Format | Description |
|--------|-------------|
| Excel (.xlsx) | Universal format for data analysis |
| Parquet (.parquet) | Columnar format for Big Data and ML |
| CSV (.csv) | Universal text format |

---

## About the Database

The modern construction industry in Eurasia and the Asia-Pacific region relies on a unified ecosystem of technical standardization that serves as a common engineering language for more than 10 dynamically developing economies.

The DDC CWICR database (Construction Work Items, Components & Resources) is an attempt to harmonize standards, creating a seamless regulatory space for capital project management across multiple languages. The database covers the full spectrum of construction work: from earthworks and concrete to specialized installation operations.

## Data Sources

DDC CWICR is built on official construction cost standards from Eurasian countries that are publicly available. The database was developed in close collaboration with estimators and construction specialists from different countries, which allowed us to take into account practical aspects of working with data. The data has been systematized into a unified structure, harmonized methodologically, and presented in 11 language versions and 11 regional pricing versions for international use.

## Historical Development

The methodology of resource-based standardization of construction work has been continuously developing and improving since the 1920s - from the first production norms to modern digital reference books. Over a century, the system has evolved from manual calculations to machine-readable databases while preserving the fundamental principle: accurate recording of physical resources per unit of construction output.

The modern version integrates historical data with current market prices. In local markets, similar systems are adapted and known under national codes: ENIR, GESN, FER, NRR, ESN, AzDTN, ShNQK, MKS ChT, SNT, BNbD, Dinh Muc, Ding'e.

## Resource-Based Costing Methodology

The key value of Resource-Based Costing is the separation of unchanging production technology from the volatile financial component: it is based on the physical "first principles" of construction - standard norms for labor costs, machine time, and material consumption. These norms remain virtually unchanged regardless of which country the construction is carried out in.

This enables transparent pricing, eliminates hidden markups, and allows for Deep-Dive Audit of investments. As a result, DDC CWICR serves not just as a reference book, but as a fundamental risk management tool that has become the de facto industry standard for the macro-region over the past century.

## Database Statistics

- **55,719** work items and rates
- **27,672** unique resources
- **10+** countries of application


## Data Structure

The database contains 85 columns organized into logical groups:

### Classification Hierarchy
*10 columns*

category_type, collection_code/name, department_code/name, section_name, subsection_code/name

### Rate (Work Item)
*11 columns*

rate_code, rate_original_name, rate_unit, row_type, flags is_material/is_labor/is_machine/is_abstract

### Resources
*7 columns*

resource_code, resource_name, resource_unit, resource_quantity, resource_price_per_unit, resource_cost

### Labor
*11 columns*

count_workers/engineers/operators, labor_hours by category, cost_of_working_hours

### Machinery & Equipment
*12 columns*

machine_class, personnel_operator_grade, electricity_consumption_kwh, electricity_cost

### Price Variants
*16 columns*

price_est_min/max/median/mean, position_count, tech_group

### Mass
*3 columns*

mass_name, mass_value, mass_unit

## Use Cases

- **Cost Benchmarking** - Compare costs across regions
- **Price Indexation** - Track dynamics
- **Localization** - Adapt to local conditions
- **ETL/BI Pipelines** - Extract and transform data
- **AI/ML Training** - Train models
- **CAD (BIM) 5D Integration** - Auto-assign rates
- **Tender Estimation** - Quick estimates
- **CO2 Calculation** - Calculate carbon footprint
- **Deep-Dive Audit** - Technical audit


## Geographic Coverage

The methodology and database are applied in various adaptations in the following regions:

- **Central Eurasia (CIS)**: Belarus, Kazakhstan, Kyrgyzstan, Russia, Tajikistan, Turkmenistan, Uzbekistan
- **Caucasus**: Armenia, Azerbaijan, Georgia
- **Eastern Europe**: Moldova, Ukraine
- **East Asia (Quota System)**: China (Ding'e), Mongolia (BNbD), Vietnam (Dinh Muc)
- **International Projects**: Bangladesh, Egypt, Turkey
- **Historical Application (1950-1990)**: Bulgaria, Czechoslovakia, Hungary


## Collaboration and Development

We are open to dialogue with the professional community. Your experience using the database in real projects helps improve the platform and expand its capabilities. Share use cases, suggest improvements, and participate in discussions.

- **GitHub**: [github.com/datadrivenconstruction](https://github.com/datadrivenconstruction)
- **Telegram**: [t.me/datadrivenconstruction](https://t.me/datadrivenconstruction)
- **LinkedIn**: [linkedin.com/company/datadrivenconstruction](https://linkedin.com/company/datadrivenconstruction)


## Consulting and Training

We work with leading construction, engineering, consulting agencies and technology firms around the world to help them implement open data principles, automate CAD/BIM processing and build robust ETL pipelines.

If you would like to test this solution with your own data, or are interested in adapting the workflow to real project tasks, feel free to contact us. Our team delivers hands-on workshops, provides strategic consulting, and develops prototypes tailored to real project processes.

We actively support organizations seeking practical solutions for digital transformation and interoperability, focusing on data quality and classification challenges, and driving the adoption of open and automated workflows.

Contact us for a free consultation where we'll discuss your challenges and demonstrate how n8n automation can transform your operations. Reach out via Email at info@datadrivenconstruction.io or visit our website at datadrivenconstruction.io to learn more about our services.



## Support the Project

If you find our tools and databases useful and would like to see more applications for the construction industry, please star our repositories on GitHub. This helps the project grow and allows you to receive notifications about new releases.

Based on DDC CWICR, you can build automated pipelines and workflows for integration with CAD (BIM), tendering systems, and BI platforms. New workflows, tools, and ready-made solutions are regularly published on GitHub and the project website. Subscribe to updates to be the first to access new releases.

- **CAD (BIM) Data Agents & Workflows + AI**: [github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)
- **OpenConstructionEstimate DDC CWICR**: [github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR)


## Language Versions

Documentation is available in 11 languages:

- **Arabic / العربية** (Dubai) - Middle East
- **Chinese / 中文** (Shanghai) - East Asia
- **Deutsch** (Berlin) - Central Europe
- **English** (Toronto) - North America
- **English** (USA) - United States
- **English** (UK) - United Kingdom
- **Español** (Barcelona) - Iberia
- **Français** (Paris) - Western Europe
- **Hindi / हिन्दी** (Mumbai) - South Asia
- **Português** (São Paulo) - Latin America
- **Russian / Русский** (St. Petersburg) - CIS


## Resources

- **Usage Example:** https://openconstructionestimate.com
- **Website:** https://datadrivenconstruction.io


---

### Unlock the Power of Data in Construction
Move to full-cycle data management where only unified structured data & processes remain and where your data is yours

---

*[Artem Boiko, 2025](https://www.linkedin.com/in/boikoartem/)*
