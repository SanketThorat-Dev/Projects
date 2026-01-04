# 🚀 End-to-End DevSecOps & Kubernetes Portfolio

This repository contains a progressive series of projects demonstrating the transition from **QA Engineering** to **DevOps/Site Reliability Engineering**. 

## 🛠️ Tech Stack & Skills
* **CI/CD:** GitHub Actions, Docker Multi-stage Builds
* **Infrastructure as Code:** Terraform
* **Orchestration:** Kubernetes (Minikube), Helm
* **Security:** Trivy Container Scanning
* **Observability:** Prometheus, Grafana

---

## 📁 Projects Overview

### 1. [Quality-Gated CI/CD Pipeline](./quality-gated-pipeline)
**Goal:** Automate code quality and security for a Python/Flask application.
* **QA Focus:** Integrated Flake8 (Linting) and Pytest (Unit Testing) as mandatory gates.
* **SecOps:** Integrated Trivy to scan Docker images for HIGH/CRITICAL vulnerabilities.
* **Outcome:** A "Ship with Confidence" pipeline that prevents bad code from reaching production.

### 2. [Self-Healing K8s Infrastructure](./kubernetes-infrastructure)
**Goal:** Provision a resilient local cloud environment using IaC.
* **IaC:** Used **Terraform** to manage Kubernetes Namespaces.
* **Orchestration:** Deployed 2-replica application sets with **Liveness Probes**.
* **Outcome:** Verified **Self-Healing** capabilities by manually terminating pods and observing automatic restoration.

### 3. [Cloud-Scale Observability Stack](./monitoring-stack)
**Goal:** Implement a professional monitoring and alerting system.
* **Deployment:** Used **Helm** to deploy the Prometheus/Grafana stack.
* **Visualization:** Created dashboards to track CPU, Memory, and Pod Lifecycle events.
* **Outcome:** Achieved 100% visibility into infrastructure health, reducing MTTD (Mean Time to Detection).

---

## 📈 My Transition Journey
As a former **QA Engineer**, I bridge the gap between "Does it work?" and "Does it scale?" My approach prioritizes:
1.  **Shift-Left Security** (Scanning early).
2.  **Automated Quality Gates** (Testing as code).
3.  **Observability-Driven Development** (Monitoring as a standard).