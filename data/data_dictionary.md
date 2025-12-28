## production_batches.csv

| Column | Description |
|------|------------|
| batch_id | Unique production batch identifier |
| plant | Manufacturing plant |
| country | Country of plant |
| product | Product name |
| production_date | Date of production |
| units_produced | Total units produced |
| units_rejected | Units rejected due to quality |
| production_time_hrs | Production duration |
| delay_days | Production delay in days |
| production_cost | Total batch cost |
| quality_issue | Type of quality issue (if any) |

## distribution_shipments.csv

| Column | Description |
|------|------------|
| batch_id | Unique batch identifier (FK to production_batches) |
| region | Destination region |
| planned_delivery | Planned delivery date |
| actual_delivery | Actual delivery date |
| transport_days | Total transport duration in days |
| delivery_delay_days | Delivery delay in days (actual - planned) |
| delivery_status | Shipment status (On Time / Delayed) |
| critical_delay_ship | Flag indicating critical delivery delay |
| on_time_flag | Flag indicating on-time delivery |

## dim_plants.csv

| Column | Description |
|------|------------|
| plant | Manufacturing plant identifier (PK) |
| country | Country where the plant is located |
| plant_type | Type of plant (e.g. Solid, Biological) |
| capacity_units_per_month | Monthly production capacity |
