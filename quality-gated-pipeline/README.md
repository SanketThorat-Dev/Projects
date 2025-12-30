# Quality-Gated CI/CD Pipeline

## Overview
This project demonstrates a robust CI/CD pipeline using GitHub Actions, focusing on "Shift-Left" principles. As a transition from QA to DevOps, this project emphasizes that code is only as good as its tests.

## Tech Stack
* **Language:** Python (Flask)
* **CI/CD:** GitHub Actions
* **Testing:** Pytest
* **Linting:** Flake8
* **Containerization:** Docker
* **Security:** Trivy (Container Scanning)

## Local Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. Install dependencies: `pip install -r app/requirements.txt`
4. Run tests: `pytest tests/`

## Development Log - Week 1
* Successfully set up Python virtual environment on Windows.
* Implemented basic Flask API with two endpoints: `/` and `/health`.
* Configured Pytest and verified 100% test pass rate locally.
## Containerization
* Implemented a **Multi-stage Dockerfile** to optimize image size and security.
* Integrated **Automated Testing** into the build process; images will not build if tests fail.
## CI/CD Automation
* **GitHub Actions:** Integrated a CI pipeline that triggers on every push.
* **Automated Quality Gates:** The pipeline automatically runs Flake8 (linting) and Pytest (unit testing).
* **Build Verification:** Ensures the Docker image builds successfully in a clean environment before completion.