from flask import Flask, render_template
from model import detect_anomaly

app = Flask(__name__)

@app.route("/")
def home():
    values, anomalies = detect_anomaly()
    return render_template("index.html", values=values, anomalies=anomalies)

if __name__ == "__main__":
    app.run(debug=True)