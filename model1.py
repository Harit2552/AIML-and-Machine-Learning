import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

print("Loading processed dataset...")
df = pd.read_csv("processed_cars.csv")

y = df["price_rupees"]
X = df.drop(columns=["price_rupees"])

cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
print("Encoding categorical columns:", cat_cols)

X = pd.get_dummies(X, columns=cat_cols, drop_first=True)
feature_cols = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=300, max_depth=20, random_state=42, n_jobs=-1
)

print("Training model...")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nEvaluation:")
print("R2:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MAE:", mean_absolute_error(y_test, y_pred))

joblib.dump(model, "car_price_model.pkl")
joblib.dump(feature_cols, "feature_columns.pkl")

print("\nModel saved → car_price_model.pkl")
