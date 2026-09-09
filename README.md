# 🚀 MLOps Learning Roadmap

> A structured, hands-on roadmap for learning **Machine Learning Operations (MLOps)** — from Linux and Git fundamentals to experiment tracking, containerization, CI/CD, Kubernetes, cloud deployment, and production monitoring.

---

## 📌 About This Repository

This repository documents my journey of learning **MLOps from fundamentals to production-level machine learning systems**.

The goal is not only to understand individual MLOps tools, but to understand how they work together to build a complete machine learning lifecycle.

A traditional machine learning workflow often looks like:

```text
Data
  ↓
Preprocessing
  ↓
Model Training
  ↓
Evaluation
  ↓
Accuracy = 92%
  ↓
Done ❌
```

A production MLOps workflow extends much further:

```text
Data
  ↓
Data Versioning
  ↓
Data Pipeline
  ↓
Model Training
  ↓
Experiment Tracking
  ↓
Model Registry
  ↓
Testing
  ↓
Containerization
  ↓
CI/CD
  ↓
Cloud Deployment
  ↓
Monitoring
  ↓
Retraining
```

The objective of this repository is to understand and eventually implement this complete workflow.

---



---

# 🎯 Learning Goals

By completing this roadmap, I aim to understand how to:

- Build reproducible machine learning pipelines
- Version code, datasets, and model artifacts
- Track machine learning experiments
- Organize ML projects using production-style architecture
- Package ML applications using Docker
- Build automated CI/CD pipelines
- Deploy ML applications to cloud infrastructure
- Scale ML services using Kubernetes
- Monitor deployed applications
- Understand the complete ML model lifecycle
- Build an end-to-end production-ready MLOps project

---

# 🧠 What is MLOps?

**MLOps = Machine Learning + DevOps + Data Engineering**

MLOps introduces engineering practices that make machine learning systems:

- Reproducible
- Automated
- Testable
- Deployable
- Scalable
- Observable
- Maintainable

The complete lifecycle can be represented as:

```text
                        ┌─────────────────────┐
                        │       DATA          │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   DATA VERSIONING   │
                        │        DVC          │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   DATA PIPELINE     │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   MODEL TRAINING    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ EXPERIMENT TRACKING │
                        │       MLflow        │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   MODEL ARTIFACT    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │       DOCKER        │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │       CI/CD         │
                        │   GitHub Actions    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │     KUBERNETES      │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    CLOUD / AWS      │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │     MONITORING      │
                        │      Grafana        │
                        └──────────┬──────────┘
                                   │
                                   ▼
                              RETRAINING
```

---

# 🗺️ MLOps Roadmap

The roadmap is divided into the following major areas:

```text
01. MLOps Fundamentals
        ↓
02. Linux
        ↓
03. Git & GitHub
        ↓
04. Data Versioning with DVC
        ↓
05. Cloud Fundamentals
        ↓
06. Experiment Tracking with MLflow
        ↓
07. Docker
        ↓
08. End-to-End ML Pipeline
        ↓
09. CI/CD
        ↓
10. Kubernetes
        ↓
11. AWS SageMaker
        ↓
12. Production Monitoring
```

---

# 01 — MLOps Fundamentals

## Topics

- What is MLOps?
- Why do we need MLOps?
- Machine Learning Lifecycle
- ML vs MLOps
- DevOps vs MLOps
- Reproducibility
- Automation
- Model deployment
- Model monitoring
- Model retraining
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Continuous Training

---

## Traditional ML vs MLOps

### Traditional ML

```text
Dataset
   ↓
Notebook
   ↓
Train Model
   ↓
Evaluate
   ↓
Save model.pkl
```

### Production MLOps

```text
Dataset
   ↓
Version Data
   ↓
Validate Data
   ↓
Transform Data
   ↓
Train Model
   ↓
Track Experiment
   ↓
Register Model
   ↓
Test
   ↓
Package
   ↓
Deploy
   ↓
Monitor
   ↓
Retrain
```

---

# 02 — Linux for MLOps

Most ML production infrastructure runs on Linux.

Examples include:

- AWS EC2
- Docker containers
- Kubernetes nodes
- Cloud servers
- CI/CD runners
- ML inference servers

---

## Architecture

```text
Local Machine
      ↓
     SSH
      ↓
Linux Server
      ↓
Python Environment
      ↓
ML Application
```

---

## Important Linux Commands

### Navigation

```bash
pwd
ls
ls -la
cd folder_name
cd ..
```

### Files and Directories

```bash
mkdir project
touch file.txt
cp source destination
mv source destination
rm file.txt
rm -rf directory
```

### File Inspection

```bash
cat file.txt
head file.txt
tail file.txt
less file.txt
```

### System

```bash
whoami
uname -a
df -h
free -h
top
```

### Package Installation

```bash
sudo apt update
sudo apt upgrade
sudo apt install package-name
```

---

# 03 — AWS EC2 Fundamentals

Amazon EC2 allows us to create virtual machines in the cloud.

```text
AWS
 │
 └── EC2
      │
      └── Linux Server
             │
             ├── Python
             ├── Git
             ├── Docker
             └── ML Application
```

---

## Concepts to Understand

- EC2 instance
- Virtual machine
- SSH
- Public IP
- Private IP
- Security Groups
- Ports
- Key pairs
- Linux server administration

---

# 04 — Git & GitHub

Git provides **source code version control**.

GitHub provides a remote platform to store and collaborate on Git repositories.

---

## Git Workflow

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
       ↓
  git commit
       ↓
Local Repository
       ↓
   git push
       ↓
GitHub Repository
```

---

## Important Commands

```bash
git init
git clone <repository-url>

git status

git add .
git commit -m "commit message"

git push
git pull
```

---

## Branching

Instead of developing directly on `main`:

```text
main
 │
 ├── feature/data-pipeline
 │
 ├── feature/model-training
 │
 ├── feature/api
 │
 └── feature/deployment
```

Development workflow:

```text
Feature Branch
      ↓
Development
      ↓
Testing
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge
      ↓
Main
```

---

# 05 — Data Version Control with DVC

Git works extremely well for code.

However, machine learning systems also need to version:

- Large datasets
- Model artifacts
- Pipeline outputs
- Experiments

This is where **DVC — Data Version Control** becomes useful.

---

## Git + DVC

```text
                ML PROJECT
                    │
          ┌─────────┴─────────┐
          │                   │
         Git                 DVC
          │                   │
       Source Code          Dataset
       Config Files         Models
       Scripts              Artifacts
```

---

## DVC Initialization

```bash
git init

dvc init
```

---

## Track Dataset

```bash
dvc add data/data.csv
```

Then:

```bash
git add data/data.csv.dvc .gitignore
git commit -m "Track dataset using DVC"
```

---

# 06 — DVC ML Pipelines

Machine learning systems usually contain multiple pipeline stages.

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
```

DVC allows us to define dependencies between these stages.

Example:

```yaml
stages:

  data_ingestion:
    cmd: python src/data_ingestion.py

  preprocessing:
    cmd: python src/preprocessing.py

  training:
    cmd: python src/model_training.py

  evaluation:
    cmd: python src/evaluation.py
```

---

## Main Concept: Reproducibility

```text
Same Code
    +
Same Data
    +
Same Parameters
    +
Same Environment
    ↓
Reproducible Model
```

---

# 07 — Cloud Fundamentals

Production machine learning systems generally require remote infrastructure.

---

## Basic Cloud Architecture

```text
User
 ↓
Internet
 ↓
Load Balancer
 ↓
Application/API
 ↓
ML Model
 ↓
Database / Object Storage
```

---

## Concepts

- Compute
- Storage
- Networking
- Virtual Machines
- Cloud APIs
- Security
- Scalability
- High Availability

---

# 08 — Experiment Tracking with MLflow

Machine learning development involves many experiments.

For example:

```text
Experiment #1

Model:
Random Forest

Accuracy:
87%
```

```text
Experiment #2

Model:
XGBoost

Accuracy:
91%
```

```text
Experiment #3

Model:
XGBoost

learning_rate = 0.01

Accuracy:
93%
```

Managing these manually becomes difficult.

MLflow helps track them.

---

## MLflow Tracks

```text
Experiment
 │
 ├── Parameters
 │     ├── learning_rate
 │     ├── max_depth
 │     ├── epochs
 │     └── batch_size
 │
 ├── Metrics
 │     ├── accuracy
 │     ├── precision
 │     ├── recall
 │     ├── F1
 │     └── RMSE
 │
 ├── Artifacts
 │     ├── model.pkl
 │     ├── confusion_matrix.png
 │     └── plots
 │
 └── Metadata
```

---

## Basic MLflow Example

```python
import mlflow

with mlflow.start_run():

    mlflow.log_param("learning_rate", 0.01)

    mlflow.log_metric("accuracy", 0.93)

    mlflow.sklearn.log_model(
        model,
        "model"
    )
```

---

# 09 — MLflow + DagsHub

Local experiment tracking works for an individual developer.

Teams need centralized experiment tracking.

```text
Developer
    ↓
MLflow
    ↓
DagsHub
    ↓
Shared Experiment Dashboard
```

Team members can compare:

- Models
- Metrics
- Hyperparameters
- Artifacts
- Experiment history

---

# 10 — Docker

One of the most important MLOps concepts.

Docker solves the classic problem:

> "It works on my machine."

Docker packages:

```text
Application
+
Python
+
Dependencies
+
System Libraries
+
Configuration
+
ML Model
```

into a portable environment.

---

## Docker Workflow

```text
Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
docker run
    ↓
Docker Container
```

---

# Docker Image vs Container

### Docker Image

A blueprint/template used to create containers.

### Docker Container

A running instance of a Docker image.

```text
Docker Image
    │
    ├── Container #1
    ├── Container #2
    └── Container #3
```

---

# Docker Commands

```bash
docker build -t ml-app .
```

```bash
docker run ml-app
```

```bash
docker ps
```

```bash
docker ps -a
```

```bash
docker stop <container-id>
```

```bash
docker images
```

---

# Dockerfile Example

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

## Dockerfile Flow

```text
Base Python Image
       ↓
Create Working Directory
       ↓
Copy Dependencies
       ↓
Install Dependencies
       ↓
Copy Source Code
       ↓
Launch Application
```

---

# 11 — End-to-End MLOps Project

This is one of the most important sections of the roadmap.

The goal is to connect everything learned so far.

---

## Pipeline

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Experiment Tracking
   ↓
Model Artifact
   ↓
Prediction API
   ↓
Docker
   ↓
Deployment
```

---

# Recommended Project Structure

```text
mlops-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── artifacts/
│
├── notebooks/
│   └── experimentation.ipynb
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── utils/
│   │   └── common.py
│   │
│   ├── logger.py
│   └── exception.py
│
├── tests/
│   ├── test_data.py
│   └── test_model.py
│
├── app.py
│
├── Dockerfile
│
├── dvc.yaml
├── dvc.lock
│
├── requirements.txt
│
├── setup.py
│
├── .gitignore
│
└── README.md
```

---

# 12 — CI/CD

CI/CD automates testing, building, and deploying applications.

---

# Continuous Integration — CI

When a developer pushes code:

```text
Developer
    ↓
git push
    ↓
GitHub
    ↓
CI Triggered
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
Code Quality Checks
    ↓
Build Application
```

---

# Continuous Delivery / Deployment — CD

After CI passes:

```text
Successful CI
     ↓
Build Docker Image
     ↓
Push Docker Image
     ↓
Deploy
     ↓
Production
```

---

# 13 — GitHub Actions

GitHub Actions allows automated workflows directly from GitHub.

---

## Example Pipeline

```text
git push
    ↓
GitHub Actions
    ↓
Checkout Code
    ↓
Install Python
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Push Docker Image
    ↓
Deploy
```

---

## Example GitHub Actions Workflow

```yaml
name: ML CI Pipeline

on:
  push:
    branches:
      - main

  pull_request:
    branches:
      - main

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

---

# 14 — Jenkins

Jenkins is another popular CI/CD automation server.

It is commonly found in enterprise infrastructure.

---

## Architecture

```text
GitHub
   ↓
Jenkins Server
   ↓
Jenkins Pipeline
   ↓
Build
   ↓
Test
   ↓
Dockerize
   ↓
Deploy
```

---

## Jenkins Pipeline Concept

```text
Checkout
   ↓
Build
   ↓
Test
   ↓
Docker Build
   ↓
Push Image
   ↓
Deploy
```

---

## Important Jenkins Concepts

- Jenkins Server
- Jobs
- Pipelines
- Agents
- Stages
- Jenkinsfile
- Plugins
- Credentials
- GitHub Webhooks

---

# 15 — CircleCI

CircleCI provides another approach to CI/CD automation.

The underlying idea remains similar.

```text
Git Push
   ↓
CircleCI
   ↓
Test
   ↓
Build
   ↓
Package
   ↓
Deploy
```

---

## Important Learning Point

Do not treat:

```text
GitHub Actions
Jenkins
CircleCI
```

as three completely unrelated subjects.

They are different implementations of the same core concept:

```text
                CI/CD

Code Change
    ↓
Automated Testing
    ↓
Automated Build
    ↓
Artifact Creation
    ↓
Deployment
```

For this roadmap, **GitHub Actions is the primary CI/CD tool to master deeply**.

---

# 16 — Kubernetes

Docker allows applications to run inside containers.

But production systems may require hundreds or thousands of containers.

Kubernetes manages them.

---

# Basic Kubernetes Architecture

```text
                    Kubernetes Cluster
                           │
                    Control Plane
                           │
              ┌────────────┼────────────┐
              │            │            │
            Node 1       Node 2       Node 3
              │            │            │
             Pods         Pods         Pods
              │            │            │
          Containers   Containers   Containers
```

---

# Important Kubernetes Concepts

## Cluster

A complete Kubernetes environment.

## Node

A machine inside the cluster.

## Pod

The smallest deployable Kubernetes unit.

## Deployment

Defines how applications should run.

## Replica

Multiple copies of an application.

## Service

Provides network access to pods.

---

# ML Model Scaling Example

```text
                       Users
                         ↓
                    Load Balancer
                         ↓
                 Kubernetes Service
                         ↓
              ┌──────────┼──────────┐
              │          │          │
             Pod        Pod        Pod
              │          │          │
            ML API     ML API     ML API
              │          │          │
            Model      Model      Model
```

This makes it possible to scale ML inference.

---

# 17 — AWS SageMaker

Amazon SageMaker is AWS's managed machine learning platform.

---

## Traditional Approach

You may need to manually manage:

```text
EC2
+
Docker
+
Training Infrastructure
+
Storage
+
Deployment
+
Model Servers
+
Monitoring
```

SageMaker provides managed services around many of these tasks.

---

## SageMaker Lifecycle

```text
Dataset
   ↓
SageMaker Training
   ↓
Experiments
   ↓
Model Artifact
   ↓
Model Registry
   ↓
SageMaker Endpoint
   ↓
Predictions
```

---

# Important SageMaker Concepts

- Training Jobs
- Processing Jobs
- Model Registry
- Endpoints
- Real-time Inference
- Batch Inference
- S3 integration
- IAM roles

---

# 18 — Production Monitoring

Deployment is not the end of the machine learning lifecycle.

Once a model is deployed, it needs to be monitored.

---

## Production Lifecycle

```text
Model
   ↓
Predictions
   ↓
Metrics + Logs
   ↓
Monitoring
   ↓
Alerts
   ↓
Investigation
   ↓
Retraining
```

---

# 19 — Grafana

Grafana provides dashboards for monitoring applications and infrastructure.

---

## Metrics We Can Monitor

### Infrastructure Metrics

```text
CPU Usage
Memory Usage
Disk Usage
Network Usage
```

### API Metrics

```text
Requests / Second
Latency
HTTP Errors
Availability
```

### ML Metrics

```text
Prediction Distribution
Model Accuracy
Model Confidence
Feature Distribution
Data Drift
Model Drift
```

---

## Example Monitoring Dashboard

```text
┌──────────────────────────────────┐
│      ML PRODUCTION SYSTEM        │
├──────────────────────────────────┤
│                                  │
│ Requests/sec        340          │
│ Prediction latency  120 ms       │
│ CPU                  62%         │
│ Memory               4.2 GB      │
│ Error Rate            0.3%       │
│                                  │
└──────────────────────────────────┘
```

---

# 🔄 Complete End-to-End MLOps Architecture

```text
                         Developer
                            │
                            ▼
                     Git / GitHub
                            │
                            ▼
                    Source Code
                            │
               ┌────────────┴────────────┐
               │                         │
               ▼                         ▼
             DVC                       MLflow
               │                         │
               ▼                         ▼
         Data Versioning         Experiment Tracking
               │                         │
               └────────────┬────────────┘
                            │
                            ▼
                      ML Pipeline
                            │
                            ▼
                     Model Training
                            │
                            ▼
                    Model Evaluation
                            │
                            ▼
                      Model Artifact
                            │
                            ▼
                          Docker
                            │
                            ▼
                      Docker Image
                            │
                            ▼
                     GitHub Actions
                            │
                            ▼
                          CI/CD
                            │
                            ▼
                       Kubernetes
                            │
                            ▼
                         AWS
                            │
                            ▼
                    Production API
                            │
                            ▼
                        Grafana
                            │
                            ▼
                       Monitoring
                            │
                            ▼
                        Retraining
```

---

# 🧩 The 8 Core MLOps Concepts

Instead of thinking about MLOps as dozens of unrelated technologies, I am organizing my learning around **8 core concepts**.

---

## 1️⃣ Version Control

### Tool

**Git + GitHub**

Purpose:

```text
Track source code
Manage collaboration
Maintain history
Review changes
```

---

## 2️⃣ Data & Pipeline Versioning

### Tool

**DVC**

Purpose:

```text
Dataset Versioning
Model Versioning
Pipeline Reproducibility
```

---

## 3️⃣ Experiment Tracking

### Tool

**MLflow**

Purpose:

```text
Parameters
Metrics
Models
Artifacts
Experiments
```

---

## 4️⃣ Containerization

### Tool

**Docker**

Purpose:

```text
Reproducible Environment
Portable ML Application
Dependency Management
```

---

## 5️⃣ CI/CD

### Primary Tool

**GitHub Actions**

Additional exposure:

```text
Jenkins
CircleCI
```

Purpose:

```text
Test
Build
Package
Deploy
```

---

## 6️⃣ Container Orchestration

### Tool

**Kubernetes**

Purpose:

```text
Scale containers
Restart failed containers
Manage replicas
Load balance services
```

---

## 7️⃣ Cloud ML

### Tools

```text
AWS
EC2
SageMaker
```

Purpose:

```text
Training
Hosting
Scaling
Deployment
```

---

## 8️⃣ Monitoring

### Tool

**Grafana**

Purpose:

```text
Infrastructure Monitoring
API Monitoring
Model Monitoring
Alerting
```

---

# ⭐ Learning Priority

Not every tool needs the same level of mastery.

---

## 🔥 Learn Deeply

```text
Git & GitHub
      ↓
DVC
      ↓
MLflow
      ↓
Docker
      ↓
End-to-End ML Pipeline
      ↓
GitHub Actions
      ↓
Kubernetes
      ↓
Monitoring
```

These form the core MLOps foundation.

---

## 🟡 Learn Well

```text
Linux
AWS
EC2
SageMaker
```

Understand how ML applications interact with cloud infrastructure.

---

## 🟢 Understand Conceptually First

```text
Jenkins
CircleCI
```

The main objective is understanding CI/CD.

Once one CI/CD system is understood deeply, learning another becomes much easier.

---

# ✅ Learning Progress Tracker

## MLOps Fundamentals

- [ ] Understand MLOps
- [ ] Understand ML lifecycle
- [ ] Understand reproducibility
- [ ] Understand automation
- [ ] Understand model deployment
- [ ] Understand model monitoring

---

## Linux

- [ ] Linux navigation
- [ ] File management
- [ ] Package management
- [ ] Process management
- [ ] SSH
- [ ] Linux server basics

---

## Git & GitHub

- [ ] Git initialization
- [ ] Commits
- [ ] Push / Pull
- [ ] Branches
- [ ] Merge
- [ ] Pull Requests
- [ ] `.gitignore`

---

## DVC

- [ ] Install DVC
- [ ] Initialize DVC
- [ ] Track dataset
- [ ] Understand `.dvc` files
- [ ] Create DVC pipeline
- [ ] Reproduce pipeline

---

## MLflow

- [ ] Create experiment
- [ ] Create run
- [ ] Log parameters
- [ ] Log metrics
- [ ] Log model
- [ ] Log artifacts
- [ ] Compare experiments
- [ ] Understand Model Registry

---

## Docker

- [ ] Understand images
- [ ] Understand containers
- [ ] Write Dockerfile
- [ ] Build Docker image
- [ ] Run container
- [ ] Expose ports
- [ ] Understand Docker networking
- [ ] Push image to registry

---

## End-to-End ML Pipeline

- [ ] Data ingestion
- [ ] Data validation
- [ ] Data transformation
- [ ] Model training
- [ ] Model evaluation
- [ ] Prediction pipeline
- [ ] Logging
- [ ] Exception handling
- [ ] Configuration management

---

## CI/CD

- [ ] Understand CI
- [ ] Understand CD
- [ ] Create GitHub Action
- [ ] Run automated tests
- [ ] Build Docker image
- [ ] Push Docker image
- [ ] Deploy automatically

---

## Jenkins

- [ ] Understand Jenkins server
- [ ] Understand jobs
- [ ] Understand pipeline
- [ ] Understand Jenkinsfile
- [ ] Connect GitHub
- [ ] Build basic pipeline

---

## Kubernetes

- [ ] Understand cluster
- [ ] Understand node
- [ ] Understand pod
- [ ] Understand deployment
- [ ] Understand service
- [ ] Understand replicas
- [ ] Deploy Docker application
- [ ] Scale application

---

## AWS

- [ ] Understand EC2
- [ ] Understand S3
- [ ] Understand IAM
- [ ] Deploy application
- [ ] Understand networking

---

## SageMaker

- [ ] Training job
- [ ] Model artifact
- [ ] Model registry
- [ ] Endpoint
- [ ] Real-time inference

---

## Monitoring

- [ ] Understand application monitoring
- [ ] Understand infrastructure monitoring
- [ ] Understand model monitoring
- [ ] Understand data drift
- [ ] Understand model drift
- [ ] Build Grafana dashboard

---

# 🧪 Practical Projects

Watching tutorials alone is not enough.

Each major topic should include a small practical implementation.

---

## Project 1 — Git + ML

Build a basic ML project and manage it using Git.

```text
Dataset
   ↓
Notebook / Python
   ↓
Training
   ↓
Git Version Control
```

---

## Project 2 — DVC Pipeline

Create:

```text
Raw Data
   ↓
Preprocessing
   ↓
Training
   ↓
Evaluation
```

Track the pipeline using DVC.

---

## Project 3 — MLflow Experiment Tracking

Run multiple models:

```text
Logistic Regression
Random Forest
XGBoost
```

Track:

```text
Parameters
Metrics
Models
Artifacts
```

using MLflow.

---

## Project 4 — Dockerized ML API

Build:

```text
ML Model
   ↓
FastAPI / Flask
   ↓
Docker
   ↓
Container
```

---

## Project 5 — CI/CD ML Application

Build:

```text
GitHub
   ↓
GitHub Actions
   ↓
Tests
   ↓
Docker Build
   ↓
Deployment
```

---

## Project 6 — Kubernetes ML Deployment

Deploy the Dockerized ML API using Kubernetes.

```text
Docker Image
     ↓
Kubernetes Deployment
     ↓
Multiple Pods
     ↓
Kubernetes Service
     ↓
Users
```

---

# 🏆 Final Portfolio Project

The final objective is to build **one complete production-style MLOps project**.

---

## Desired Architecture

```text
                       GitHub Repository
                              │
                              ▼
                         Source Code
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
            DVC                             MLflow
              │                               │
              ▼                               ▼
      Dataset Versioning             Experiment Tracking
              │                               │
              └──────────────┬────────────────┘
                             │
                             ▼
                       Training Pipeline
                             │
                             ▼
                       Model Evaluation
                             │
                             ▼
                       Model Registry
                             │
                             ▼
                         ML API
                             │
                             ▼
                          Docker
                             │
                             ▼
                     GitHub Actions
                             │
                             ▼
                           CI/CD
                             │
                             ▼
                        Kubernetes
                             │
                             ▼
                           AWS
                             │
                             ▼
                     Production Endpoint
                             │
                             ▼
                         Monitoring
                             │
                             ▼
                          Grafana
```

---

# 🎯 Definition of "MLOps Ready"

At the end of this roadmap, I should be able to take a machine learning model from:

```text
Jupyter Notebook
```

to:

```text
Production System
```

without treating deployment as an afterthought.

I should understand how to:

```text
Version
   ↓
Experiment
   ↓
Train
   ↓
Test
   ↓
Package
   ↓
Deploy
   ↓
Scale
   ↓
Monitor
   ↓
Retrain
```

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming | Python |
| Operating System | Linux |
| Version Control | Git |
| Code Hosting | GitHub |
| Data Versioning | DVC |
| Experiment Tracking | MLflow |
| Experiment Platform | DagsHub |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Enterprise CI/CD | Jenkins |
| CI/CD Alternative | CircleCI |
| Container Orchestration | Kubernetes |
| Cloud | AWS |
| Cloud Compute | EC2 |
| Managed ML | SageMaker |
| Monitoring | Grafana |

---

# 📖 Recommended Learning Order

```text
MLOps Fundamentals
        │
        ▼
Linux
        │
        ▼
Git + GitHub
        │
        ▼
DVC
        │
        ▼
MLflow
        │
        ▼
Docker
        │
        ▼
Build End-to-End ML Project
        │
        ▼
GitHub Actions
        │
        ▼
AWS
        │
        ▼
Kubernetes
        │
        ▼
SageMaker
        │
        ▼
Monitoring
        │
        ▼
Production MLOps Project
```

---

# 💡 Important Learning Principle

The goal is **not to memorize tools**.

Instead, understand the problem each tool solves.

| Problem | Tool |
|---|---|
| How do I version my code? | Git |
| Where do I host my code? | GitHub |
| How do I version datasets? | DVC |
| How do I reproduce pipelines? | DVC |
| How do I track ML experiments? | MLflow |
| How do I package my application? | Docker |
| How do I test automatically? | GitHub Actions |
| How do I deploy automatically? | CI/CD |
| How do I manage many containers? | Kubernetes |
| Where do I deploy ML infrastructure? | AWS |
| How do I use managed ML infrastructure? | SageMaker |
| How do I monitor production? | Grafana |

---

# 🧠 Mental Model

Whenever learning a new MLOps tool, ask:

```text
1. What problem does this tool solve?

2. Where does it fit in the ML lifecycle?

3. What goes into the tool?

4. What comes out of the tool?

5. What happens if we don't use it?

6. How does it interact with other tools?

7. How would this work in production?
```

---

# 📈 My Target Skill Level

My target is to progress through four levels.

### Level 1 — Understand

```text
I know what the technology does.
```

### Level 2 — Implement

```text
I can follow documentation and build it.
```

### Level 3 — Integrate

```text
I can connect it with other MLOps components.
```

### Level 4 — Design

```text
I can decide when and why the technology
should be used in a production ML system.
```

The final objective is **Level 3–4 competency across the core MLOps stack**.

---

# 🚀 Final Goal

Build an ML system where:

```text
Developer pushes code
        ↓
GitHub detects change
        ↓
CI runs tests
        ↓
ML pipeline executes
        ↓
Experiments tracked with MLflow
        ↓
Model validated
        ↓
Docker image created
        ↓
Image pushed to registry
        ↓
Application deployed
        ↓
Kubernetes manages containers
        ↓
Cloud hosts infrastructure
        ↓
Monitoring collects metrics
        ↓
Alerts detect problems
        ↓
Model can eventually be retrained
```

When I can build and explain that system end-to-end, I will consider the core MLOps roadmap complete.

---

# 📌 Current Status

```text
Status: 🟡 Learning in Progress
```

I will continue updating this repository as I complete each topic and add hands-on implementations.

---

# 🤝 Connect

If you are also learning MLOps, Machine Learning Engineering, or production AI systems, feel free to connect and collaborate.

---

## ⭐ Repository Goal

This repository will evolve from:

```text
MLOps Learning Notes
```

into:

```text
MLOps Notes
      +
Hands-On Examples
      +
Mini Projects
      +
End-to-End Production Project
      +
Portfolio Repository
```

---

## 📚 Key Takeaway

> **MLOps is not about learning a collection of tools. It is about building a reliable system that can take machine learning from experimentation to production and keep it running successfully.**

---

### 🚀 Learn → Build → Automate → Deploy → Monitor → Improve
