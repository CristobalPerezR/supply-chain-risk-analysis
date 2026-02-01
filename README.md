# Supply Chain Risk Analysis

## Overview

This repository contains an end-to-end analytical project focused on **supply chain risk**, using the *DataCo Smart Supply Chain* public dataset.

The project emphasizes:
- Clear data-layer separation
- Explicit ETL decisions
- Reproducibility and traceability
- Analytical readiness rather than business dashboards

This is a **data science–oriented project**, not a production data platform.

## Problem framing

Modern supply chains are exposed to multiple sources of risk:
- Delivery delays
- Logistics inefficiencies
- Geographic and operational bottlenecks
- Financial loss due to late or failed orders

The goal of this project is to prepare and structure the data in a way that allows:
- Exploratory risk analysis
- Identification of delay patterns
- Downstream modeling or BI use without embedding business assumptions too early


## Dataset

- **Source**: DataCo Smart Supply Chain for Big Data Analysis  
- **Provider**: Mendeley Data  
- **Link**: https://data.mendeley.com/datasets/8gx2fvg2k6/5  

The dataset is treated as an **external system**. No assumptions are made about data quality or correctness beyond what is explicitly documented.

---

## Repository structure

```text
.
├── data/
│   ├── raw/          # Origina data
│   └── processed/    # Cleaned and standardized analytical layer
│
├── src/
│   └── etl/
│       ├── extract.py
│       ├── transform.py
│       └── load.py
│
├── docs/
│   └── ETL.md        # ETL decisions, assumptions, and trade-offs
│
└── README.md
```

## Data layers

The project follows a layered data architecture:

### Processed layer

* Cleaned and standardized version of the raw data
* Irrelevant or high-risk columns removed
* Intended for analytical consumption
* No aggregation or business KPIs encoded

Detailed ETL rationale is documented in [ETL.md](https://github.com/CristobalPerezR/supply-chain-risk-analysis/blob/main/docs/ETL.md)

## ETL philosophy

The ETL pipeline is designed with the following principles:

* Deterministic and reproducible transformations
* Explicit documentation of trade-offs
* Separation between data preparation and business interpretation
* Avoidance of premature optimization

This repository documents why decisions were made, not only how.

## Current Status
* ☑️ Dataset exploration
* ☑️ ETL design and documentation
* ☑️ Extraction implementation
* ⬜ Transformation logic
* ⬜ Database desing
* ⬜ Load Step
* ⬜ Analytical exploration
* ⬜ Modeling (optional)

## Non-goals

* This project intentionally does not:
* Act as a production-ready data warehouse
* Provide real-time ingestion
* Encode business KPIs or financial decisions
* Optimize for dashboard performance