import pandas as pd
import numpy as np
import random
from datetime import timedelta

# Cargar producción
production_df = pd.read_csv("production_batches.csv")

regions = [
    ("North America", 2),
    ("Central America", 3),
    ("South America", 3),
    ("Western Europe", 4),
    ("Eastern Europe", 5),
    ("South Asia", 6),
    ("East Asia", 7)
]

rows = []

for _, row in production_df.iterrows():
    shipments = np.random.choice([1, 2], p=[0.7, 0.3])
    for _ in range(shipments):
        region, base_days = random.choice(regions)
        planned = pd.to_datetime(row["production_date"]) + timedelta(days=base_days)

        # Delay lógico
        prod_delay = row["delay_days"]
        transport_delay = np.random.choice(
            [0,1,2,3,4],
            p=[0.6,0.2,0.1,0.06,0.04]
        )

        total_delay = int(prod_delay) + int(transport_delay)
        actual = planned + timedelta(days=total_delay)
        status = "On-time" if total_delay <= 1 else "Delayed"

        rows.append([
            row["batch_id"],
            region,
            planned.date(),
            actual.date(),
            base_days + transport_delay,
            status
        ])

distribution_df = pd.DataFrame(rows, columns=[
    "batch_id",
    "region",
    "planned_delivery",
    "actual_delivery",
    "transport_days",
    "delivery_status"
])

# Limitar tamaño a ~1000
distribution_df = distribution_df.sample(n=min(1000, len(distribution_df)), random_state=42)

distribution_df.to_csv("distribution.csv", index=False)
