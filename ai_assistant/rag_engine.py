import json
import os


def retrieve_knowledge(query):

    knowledge_path = "knowledge_base"

    matched_documents = []

    for file_name in os.listdir(knowledge_path):

        file_path = os.path.join(
            knowledge_path,
            file_name
        )

        with open(file_path, "r") as file:

            content = file.read()

            if query.lower() in content.lower():

                matched_documents.append(content)

    if matched_documents:
        return matched_documents

    return ["No operational knowledge found."]


def analyze_incident(incident_type):

    knowledge_base = {

        "High Latency": {
            "cause": "Backend processing delays or overloaded service instances.",
            "solution": "Scale service replicas, optimize API execution, or reduce blocking operations.",
            "knowledge": retrieve_knowledge("latency"),
        },

        "High Error Rate": {
            "cause": "Application instability, failed dependencies, or server exceptions.",
            "solution": "Inspect server logs, restart failed services, and verify backend dependencies.",
            "knowledge": retrieve_knowledge("failures"),
        }

    }

    return knowledge_base.get(
        incident_type,
        {
            "cause": "Unknown operational anomaly detected.",
            "solution": "Further investigation required.",
            "knowledge": ["No operational guidance available."]
        }
    )


def analyze_logs():

    try:

        with open("system_logs.json", "r") as file:
            logs = json.load(file)

    except:
        return ["No logs available for analysis."]

    error_count = 0
    latency_issues = 0

    for log in logs:

        if log["type"] == "ERROR":
            error_count += 1

        if "latency" in log["message"].lower():

            try:

                latency = float(
                    log["message"].split(":")[1]
                    .replace("ms", "")
                    .strip()
                )

                if latency > 1000:
                    latency_issues += 1

            except:
                pass

    summary = []

    if error_count > 3:

        summary.append(
            "Repeated server-side failures detected."
        )

    if latency_issues > 3:

        summary.append(
            "High latency spikes observed across multiple requests."
        )

    if not summary:

        summary.append(
            "System operating within normal thresholds."
        )

    return summary 

def calculate_anomaly_score(value):

    try:

        numeric_value = float(
            str(value)
            .replace("ms", "")
            .replace("%", "")
            .strip()
        )

    except:
        numeric_value = 0

    if numeric_value > 2000:

        return {
            "score": 95,
            "risk": "Critical",
            "priority": "P1",
            "action": [
                "Immediately scale backend replicas",
                "Enable emergency traffic balancing",
                "Investigate overloaded services"
            ]
        }

    if numeric_value > 1500:

        return {
            "score": 85,
            "risk": "High",
            "priority": "P2",
            "action": [
                "Optimize API execution flow",
                "Reduce blocking operations",
                "Check database latency"
            ]
        }

    if numeric_value > 1000:

        return {
            "score": 70,
            "risk": "Moderate",
            "priority": "P3",
            "action": [
                "Monitor latency trends",
                "Review service health metrics"
            ]
        }

    return {
        "score": 20,
        "risk": "Low",
        "priority": "P4",
        "action": [
            "System operating normally"
        ]
    }