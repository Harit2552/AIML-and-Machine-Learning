import pandas as pd
import numpy as np

print("Loading dataset...")
df = pd.read_csv("cleaned_used_cars_data.csv")

# Drop rows with missing price
df = df.dropna(subset=["price"])

# Convert price from lakhs → rupees
df["price_rupees"] = df["price"] * 100000

# Extract only useful columns
df = df[[
    "car_make", "car_model", "car_age", "engine", "fuel_type",
    "kilometers_driven", "location", "mileage", "power",
    "region", "seats", "transmission", "price_rupees"
]]

# Basic numeric cleaning
df["mileage"] = pd.to_numeric(df["mileage"], errors="coerce")
df["engine"] = pd.to_numeric(df["engine"], errors="coerce")
df["power"] = pd.to_numeric(df["power"], errors="coerce")

df = df.dropna()

df.to_csv("processed_cars.csv", index=False)
print("Saved processed dataset → processed_cars.csv")
