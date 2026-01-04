# Kubernetes Observability Stack

## Overview
This project implements a full-scale monitoring solution using **Prometheus** and **Grafana**. This stack provides deep visibility into cluster health, pod performance, and application metrics.

## Tech Stack
* **Package Manager:** Helm
* **Monitoring:** Prometheus
* **Visualization:** Grafana
* **Alerting:** Alertmanager (included in stack)

## How to Access
1. Run `kubectl port-forward` to map port 3000.
2. Login to Grafana at `http://localhost:3000`.