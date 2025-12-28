# Urgent Pharma Supply Chain Analysis (ETL + Tableau)

## Business Context
A pharmaceutical company requested an urgent (24h) operational analysis due to
recurring production delays, quality issues, and delivery disruptions.

The objective was to quickly consolidate production and logistics data to identify
critical plants, high-risk batches, and operational bottlenecks affecting supply continuity.

## Scope
- Industry: Pharmaceutical Manufacturing
- Time constraint: Same-day delivery (24h)
- Focus: Production efficiency, quality, logistics delays
- Tools: Python (ETL), Tableau (Reporting)

## Data Sources
- production_batches.csv: Batch-level production data
- distribution.csv: Logistics and delivery data
- plants.csv: Plant master data

Data was provided as CSV extracts from heterogeneous operational systems.

## ETL Approach
Due to time constraints, the ETL process prioritized:
- Data reliability
- Business-rule consistency
- Fast aggregation for decision-making

Transformations included:
- Data cleansing and normalization
- KPI calculation (reject rates, delays, cost per unit)
- Identification of critical batches

## Deliverables
- Clean fact tables for Tableau
- Executive and operational dashboards
- Documented assumptions and data limitations

## Notes
This project simulates a real-world urgent analytics request. Synthetic data was used
to replicate realistic operational patterns under NDA-like constraints.

## Dashboards
- Executive Overview
- Production Risk Analysis
- Logistics Performance

Published on Tableau Public.
