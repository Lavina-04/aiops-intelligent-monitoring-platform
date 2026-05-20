from prometheus_client import generate_latest
from flask import Flask, render_template
from ai_assistant.rag_engine import analyze_logs

from monitoring.metrics import (
    track_request,
    get_metrics,
    response_times
)

from monitoring.detector import detect_incidents

import json
import random
import time

app = Flask(__name__)


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
@track_request
def home():

    # Simulate latency
    time.sleep(random.uniform(1.2, 2.0))

    # Simulate failures
    if random.randint(1, 10) > 5:
        return {
            "error": "Internal Server Error"
        }, 500

    return {
        "status": "running"
    }


# -----------------------------
# DASHBOARD ROUTE
# -----------------------------
@app.route("/incidents")
def incidents():

    incidents = detect_incidents()

    try:
        with open("incident_logs.json", "r") as file:
            history = json.load(file)
    except:
        history = []

    metrics = get_metrics()

    log_summary = analyze_logs()

    return render_template(
        "dashboard.html",
        incidents=incidents,
        history=history,
        metrics=metrics,
        latency_data=response_times[-10:],
        log_summary=log_summary
    )

@app.route("/metrics")
def metrics_endpoint():

    return generate_latest(), 200, {
        "Content-Type": "text/plain"
    }

# -----------------------------
# API ROUTE
# -----------------------------
@app.route("/api/incidents")
def api_incidents():

    incidents = detect_incidents()

    metrics = get_metrics()

    return {
        "incidents": incidents,
        "metrics": metrics
    }


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
   app.run(
    host="0.0.0.0",
    port=5000,
    debug=False
)