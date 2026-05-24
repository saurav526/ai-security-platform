import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
# Example: CICIDS dataset

df = pd.read_csv("data/security_logs.csv")

# Keep numerical columns
features = [
    'duration',
    'src_bytes',
    'dst_bytes',
    'count',
    'srv_count'
]

X = df[features]

# Train anomaly detection model
model = IsolationForest(
    contamination=0.02,
    random_state=42
)


model.fit(X)

# Save model
joblib.dump(model, "anomaly_model.pkl")

print("Model trained successfully")