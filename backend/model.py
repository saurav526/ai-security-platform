import joblib
import pandas as pd

model = joblib.load("anomaly_model.pkl")

FEATURES = [
    'duration',
    'src_bytes',
    'dst_bytes',
    'count',
    'srv_count'
]


def predict_anomaly(data):
    df = pd.DataFrame([data])
    X = df[FEATURES]

    prediction = model.predict(X)[0]

    if prediction == -1:
        return "ANOMALY"

    return "NORMAL"