# ETL

## ETL vs ELT
ETL was used due of...

### Scope and intent
This document describes the **ETL decisions**, assumptions, and trade-offs for the Supply Chain Risk project. It is not a tutorial and does not document code line by line. The goal is to make explicit why certain choices were made and **what their implications are** for downstream analysis and decision-making.

## Extraction

### Source
* Public dataset: [DataCo Smart Supply Chain for Big Data Analysis](https://data.mendeley.com/datasets/8gx2fvg2k6/5)
* The source is treated as an external system over which no control is assumed.

### Extract pipeline
* Preserve the original data as faithfully as possible, prioritizing traceability over analytical usability.
* No business logic is applied at this stage.
* Missing, inconsistent, or invalid values are allowed.
* The extract layer exists primarily for traceability and reproducibility.

### Validation strategy
* Schema validation is applied to ensure:
    * Expected columns are present.
    * Basic data types can be coerced.
* All fields are nullable.
* No range checks or semantic validations are performed.

### Limitations
* Type coercion may silently convert invalid values to nulls.
* The extract layer does not detect logical inconsistencies between columns.

## Transform

### Transformation intent

The transform stage prepares the data for analytical use while keeping decisions explicit and reversible. At this stage, the goal is structural and semantic simplification, not optimization or modeling.

### Column removal

The following columns are removed because they do not contribute to analytical decision-making in the context of supply chain risk, delays, or economic loss, and may introduce unnecessary noise or privacy concerns:

* `Product Image`
* `Product Description`
* `Customer Email`
* `Customer Password`
* `Category Id`
* `Customer Fname`
* `Customer Lname`
* `Customer Street`
* `Type`
* `Customer Zipcode`
* `Order Zipcode`
* `Latitude`
* `Longitude`

### Rationale
* Image and free-text description fields are not used in quantitative analysis.
* Personally identifiable information (PII) is explicitly excluded to avoid misuse and reduce risk.
* Customer identity is not required at this stage; analysis is performed at an operational and logistical level, not at an individual level.

### Columns Renames


### Explicit non-goals

* No imputations are performed.
* No aggregation is applied.
* No business KPIs are derived.

## Load

### Target

* Transformed data is loaded into a processed schema within the same database.
* This layer serves as the input for analytical modeling and downstream data marts.

### Guarantees

* Column names are normalized.
* Data types are consistent.
* All transformations are deterministic and reproducible.

### What this layer is not

* It is not a data mart.
* It is not optimized for BI consumption.
* It does not encode business decisions or economic interpretations.

## Trade-offs and risks

* Early removal of columns simplifies the pipeline but limits future use cases that may require customer-level analysis.
* Type coercion in the extract phase prioritizes pipeline robustness over strict data fidelity.

These trade-offs are accepted deliberately and documented to ensure transparency in downstream decisions.

## Data Layers

### Raw layer
* The raw layer represents the first persisted state of the data after extraction.
* It preserves the original structure and semantics of the source dataset, allowing missing values, inconsistencies, and duplicates.
* No business logic, imputations, or semantic corrections are applied at this stage.
* Limited type coercion is performed to ensure pipeline robustness, at the cost of potential silent nulls.

### Processed layer
* The processed layer represents a cleaned and standardized version of the raw data, intended for analytical consumption.
* At this stage, columns are normalized, irrelevant attributes are removed, and data quality flags may be introduced.
* No aggregation, business KPIs, or economic interpretations are encoded in this layer.