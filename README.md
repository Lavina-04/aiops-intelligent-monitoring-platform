# AI-Powered IT Operations Monitoring Platform

## Overview

AI-Powered IT Operations Monitoring Platform is an intelligent AIOps solution designed for real-time monitoring, anomaly detection, incident management, and root cause analysis. The platform integrates modern monitoring tools with AI-driven insights to help identify operational issues and improve system reliability.

An Attendance Management System is used as a sample workload generator to produce real-time metrics for monitoring and analysis.

---

## Features

### Real-Time Monitoring

* Continuous collection of application metrics
* Request tracking and latency monitoring
* Error detection and logging
* System health monitoring

### AIOps Capabilities

* Anomaly detection based on application behavior
* AI-generated operational insights
* Root cause analysis suggestions
* Incident management dashboard
* Automated monitoring intelligence

### Visualization

* Prometheus for metrics collection
* Grafana dashboards for visualization
* Interactive charts and analytics
* Real-time operational monitoring panels

### Containerization

* Docker-based deployment
* Service orchestration using Docker Compose
* Persistent Grafana storage

---

## System Architecture

```text
Attendance Application
        │
        ▼
Prometheus Metrics Endpoint (/metrics)
        │
        ▼
Prometheus Server
        │
        ▼
Grafana Dashboards
        │
        ▼
AI Monitoring Platform
        │
        ▼
Anomaly Detection & Root Cause Analysis
```

---

## Technology Stack

* Python
* Flask
* Prometheus
* Grafana
* Docker
* Docker Compose
* HTML
* CSS
* JavaScript

---

## Project Modules

### Monitoring Dashboard

Provides real-time visualization of operational metrics.

### Incident Management

Displays detected incidents and operational events.

### AI Analysis Engine

Generates intelligent insights and possible root causes for anomalies.

### Operational Insights

Helps administrators understand system performance trends.

---

## Running the Project

### Start Docker Services

```bash
docker compose up -d
```

### Start the Monitoring Platform

```bash
python app.py
```

### Start the Test Application

```bash
python app.py
```

---

## Application URLs

### Monitoring Platform

```text
http://localhost:5001
```

### Prometheus

```text
http://localhost:9090
```

### Grafana

```text
http://localhost:3000
```

---

## Future Enhancements

* Machine Learning-based anomaly detection
* Automated incident remediation
* Predictive maintenance capabilities
* Multi-application monitoring support
* Cloud deployment integration

---

## Author

Lavina Solanki

Developed as an AIOps project focusing on intelligent IT operations monitoring, incident analysis, and operational intelligence.
