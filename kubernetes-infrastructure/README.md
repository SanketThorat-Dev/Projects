# Local Kubernetes Infrastructure with Terraform

## Overview
This project demonstrates the use of **Infrastructure as Code (IaC)** to provision a local development environment. By using Terraform and Minikube, I have created a repeatable environment that mimics a production cloud setup without the cloud costs.

## Tech Stack
* **Orchestration:** Kubernetes (Minikube)
* **IaC:** Terraform
* **Configuration:** Kubectl

## Setup Instructions
1. Start the cluster: `minikube start --driver=docker`
2. Initialize Terraform: `terraform init`
3. Apply Infrastructure: `terraform apply`
## Key Features
* **High Availability:** Configured with 2 replicas to ensure zero downtime.
* **Self-Healing:** Implemented Kubernetes Liveness Probes. If a pod fails or is deleted, the Deployment controller automatically provisions a new instance to maintain the desired state.
* **Networking:** Exposed the application via a `NodePort` Service for local accessibility.