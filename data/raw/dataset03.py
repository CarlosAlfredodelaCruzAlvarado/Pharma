import pandas as pd
import numpy as np
import random
from datetime import timedelta

plants_data = [
    ["Plant_A", "Mexico", 380000, "Solid"],
    ["Plant_B", "USA", 420000, "Solid"],
    ["Plant_C", "Germany", 130000, "Biological"],
    ["Plant_D", "India", 620000, "Solid"],
    ["Plant_E", "Brazil", 310000, "Solid"],
    ["Plant_F", "France", 150000, "Biological"],
    ["Plant_G", "Spain", 290000, "Solid"],
    ["Plant_H", "Poland", 260000, "Solid"]
]

plants_df = pd.DataFrame(plants_data, columns=[
    "plant",
    "country",
    "capacity_units_per_month",
    "plant_type"
])

plants_df.to_csv("plants.csv", index=False)
