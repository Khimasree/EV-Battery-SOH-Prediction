import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from xgboost import XGBRegressor

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("pages/data/battery_cycle_level_dataset_CLEAN_FINAL.csv")
print("Dataset Loaded Successfully!\n")

# =========================================
# BASIC CLEANING
# =========================================

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# =========================================
# FEATURE ENGINEERING
# =========================================

# Capacity Fade
df["capacity_fade"] = 1 - df["capacity"]

# Voltage–Temperature Interaction
df["volt_temp_interaction"] = df["voltage"] * df["temperature"]

# Non-linear cycle degradation
df["cycle_squared"] = df["cycle"] ** 2

# Degradation rate approximation
df["deg_rate"] = df["capacity_fade"] / df["cycle"]
df["deg_rate"].replace([np.inf, -np.inf], 0, inplace=True)

# =========================================
# FEATURE SELECTION
# =========================================

features = [
    "cycle",
    "voltage",
    "temperature",
    "capacity",
    "capacity_fade",
    "volt_temp_interaction",
    "cycle_squared",
    "deg_rate"
]

X = df[features]

# =========================================
# SOH MODEL TRAINING
# =========================================

print("Training SOH Models...\n")

y_soh = df["soh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_soh, test_size=0.2, random_state=42
)

# Random Forest
rf_model = RandomForestRegressor(n_estimators=300, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

print("Random Forest Performance:")
print("MAE:", rf_mae)
print("R2:", rf_r2)
print("RMSE:", rf_rmse)

# XGBoost
xgb_model = XGBRegressor(n_estimators=300, random_state=42)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)

xgb_mae = mean_absolute_error(y_test, xgb_pred)
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))

print("\nXGBoost Performance:")
print("MAE:", xgb_mae)
print("R2:", xgb_r2)
print("RMSE:", xgb_rmse)

# Save Best SOH Model
if xgb_r2 > rf_r2:
    joblib.dump(xgb_model, "battery_soh_model.pkl")
    best_model = xgb_model
    print("\nBest SOH Model Saved: XGBoost")
else:
    joblib.dump(rf_model, "battery_soh_model.pkl")
    best_model = rf_model
    print("\nBest SOH Model Saved: Random Forest")

# =========================================
# RUL MODEL TRAINING
# =========================================

print("\nTraining RUL Model...\n")

y_rul = df["rul"]

X_train_rul, X_test_rul, y_train_rul, y_test_rul = train_test_split(
    X, y_rul, test_size=0.2, random_state=42
)

rul_model = RandomForestRegressor(n_estimators=300, random_state=42)
rul_model.fit(X_train_rul, y_train_rul)

rul_pred = rul_model.predict(X_test_rul)

rul_mae = mean_absolute_error(y_test_rul, rul_pred)
rul_r2 = r2_score(y_test_rul, rul_pred)
rul_rmse = np.sqrt(mean_squared_error(y_test_rul, rul_pred))

print("RUL Model Performance:")
print("MAE:", rul_mae)
print("R2:", rul_r2)
print("RMSE:", rul_rmse)

joblib.dump(rul_model, "battery_rul_model.pkl")
print("\nRUL Model Saved Successfully!")

# =========================================
# FEATURE IMPORTANCE
# =========================================

print("\nTop Degradation Factors (SOH Model):")

importances = best_model.feature_importances_
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print(importance_df)