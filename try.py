import joblib
import pandas as pd

# Load model + feature columns
model = joblib.load("car_price_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

# -------- SAME SWIFT DATA YOU USED IN OLD UI --------
input_data = {
    "car_make": "MARUTI",
    "car_model": "SWIFT DZIRE",
    "car_age": 3,
    "engine": 1197,
    "fuel_type": "Petrol",
    "kilometers_driven": 3800,
    "location": "Mathura",
    "mileage": 17,
    "power": 83,
    "region": "North",
    "seats": 5,
    "transmission": "Manual"
}


# Convert to DataFrame
df = pd.DataFrame([input_data])

# One-hot encode
df_enc = pd.get_dummies(df)

# Add missing columns as zero
missing_cols = list(set(feature_cols) - set(df_enc.columns))
missing_df = pd.DataFrame(0, index=df_enc.index, columns=missing_cols)

# Align with training columns
df_final = pd.concat([df_enc, missing_df], axis=1)[feature_cols]

# Predict
price_rupees = model.predict(df_final)[0]
price_lakhs = price_rupees / 100000

print("\nPredicted Price (₹):", price_rupees)
print("Predicted Price (Lakhs):", price_lakhs)
