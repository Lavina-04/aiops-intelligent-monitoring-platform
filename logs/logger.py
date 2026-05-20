import json
from datetime import datetime


LOG_FILE = "system_logs.json"


def write_log(log_type, message, severity="INFO"):

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": log_type,
        "severity": severity,
        "message": message
    }

    try:

        with open(LOG_FILE, "r") as file:
            logs = json.load(file)

    except:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)


def log_incident(incident):

    incident_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": incident["type"],
        "severity": incident["severity"],
        "value": incident["value"]
    }

    try:

        with open("incident_logs.json", "r") as file:
            incidents = json.load(file)

    except:
        incidents = {"incidents": []}

    incidents.append(incident_entry)

    with open("incident_logs.json", "w") as file:
        json.dump(incidents, file, indent=4)