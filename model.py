import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomaly():
    data = pd.read_csv("data.csv")

    model = IsolationForest(contamination=0.2)
    data["anomaly"] = model.fit_predict(data[["value"]])

    values = data["value"].tolist()
    anomalies = data["anomaly"].tolist()

    return values, anomalies