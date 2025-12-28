import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# Parámetros base
n_batches = 800
plants = [
    ("Plant_A", "Mexico", "Solid"),
    ("Plant_B", "USA", "Solid"),
    ("Plant_C", "Germany", "Biological"),
    ("Plant_D", "India", "Solid"),
    ("Plant_E", "Brazil", "Solid"),
    ("Plant_F", "France", "Biological"),
]

products = [
    "Paracetamol 500mg", "Ibuprofen 400mg", "Amoxicillin 500mg",
    "Metformin 850mg", "Losartan 50mg", "Aspirin 100mg",
    "Insulin Glargine", "Insulin Lispro",
    "Atorvastatin 20mg", "Omeprazole 20mg",
]

quality_issues = [
    "Contamination", "Temperature deviation",
    "Equipment failure", "Process deviation"
]

start_date = datetime(2023, 7, 1)

rows = []

for i in range(n_batches):
    plant, country, plant_type = random.choice(plants)
    product = random.choice(products)
    prod_date = start_date + timedelta(days=random.randint(0, 180))
    units = random.randint(20000, 250000)

    reject_rate = np.random.beta(2, 20) if plant_type == "Solid" else np.random.beta(2, 8)
    rejected = int(units * reject_rate)

    delay = np.random.choice([0,1,2,3,4,5,6,7,8], p=[0.5,0.15,0.1,0.08,0.06,0.04,0.03,0.02,0.02])
    issue = random.choice(quality_issues) if rejected / units > 0.07 else None

    cost_base = 1.2 if plant_type == "Solid" else 6.5
    cost = units * cost_base * np.random.uniform(0.9, 1.2)

    rows.append([
        f"BCH{i:06d}", plant, country, product,
        prod_date.date(), units, rejected,
        round(np.random.uniform(8, 30), 1),
        delay, round(cost, 2), issue
    ])

production_df = pd.DataFrame(rows, columns=[
    "batch_id","plant","country","product","production_date",
    "units_produced","units_rejected","production_time_hrs",
    "delay_days","production_cost","quality_issue"
])

production_df.to_csv("production_batches.csv", index=False)
