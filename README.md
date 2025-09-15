[![API Docker Image Version](https://img.shields.io/badge/frontend-latest-blue?logo=docker)](https://hub.docker.com/repository/docker/hophopp/sentiment-api/tags)

# Sentiment Analysis MLOps Project
## Project Overview

This project implements a Sentiment Analysis API using FastAPI, trained on the IMDB Movie Reviews dataset. The project showcases an end-to-end MLOps workflow:

- **Local experimentation** with Jupyter Notebook
- **Python scripts** for training and prediction
- **Model storage**: Azure Blob Storage
- **API**: FastAPI, Dockerized for deployment
- **CI/CD pipelines**: Jenkins for model training, testing, Docker build & deployment
- **Infrastructure provisioning**: Terraform and Terraform Cloud

The goal is to provide a robust pipeline from data preparation → model training → model storage → API deployment → production-ready pipeline.

## Dataset

**IMDB Movie Reviews**
- Contains 50,000 movie reviews labeled as positive or negative
- For initial experimentation, we sampled 5,000 reviews
- Reviews are preprocessed and used for training the model with a simple TF-IDF + classifier setup

## Tech Stack & Tools

This project leverages the following technologies:

- **Programming / ML:** Python, Scikit-learn, TF-IDF  
- **API / Web Service:** FastAPI  
- **Containerization:** Docker  
- **CI/CD Pipelines:** Jenkins  
- **Cloud Infrastructure:** Terraform, Terraform Cloud  
- **Cloud Storage:** Azure Blob Storage  

## Project Workflow

### 1. Data & Model Training
- **Dataset**: IMDB Movie Reviews (50,000 labeled reviews)
- **Initial exploration**: subset of 5,000 reviews for rapid iteration
- **Preprocessing** + TF-IDF vectorization
- **Training** using Python scripts: `train.py` and `predict.py`

# Sentiment Analysis MLOps

## 2. Model Storage

Trained models are uploaded to Azure Blob Storage:

```python
python Scripts/upload_model.py
```

**Future plan:** versioned storage & backup strategies

## 3. FastAPI Application

- Serves predictions from the trained model
- Tested locally using `curl` or FastAPI test client

**Example API call:**

```bash
curl -X POST "http://localhost:8088/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I loved this movie!"}'
```

## 4. Dockerization

- Docker image for API deployment

## 5. CI/CD Pipelines (Jenkins)

### Model Pipeline (`Jenkinsfile-model`)
- Installs dependencies
- Trains the model
- Uploads model & vectorizer to Azure Blob

### API Pipeline (`Jenkinsfile-cicd`)
- Builds Docker image
- Pushes image to Docker Hub
- Deploys container

### Pipeline Stages:
1. Checkout repository
2. Run tests
3. Build Docker image (the image is built from FastAPI using the model already uploaded on Azure Blob)
4. Push Docker image to Docker Hub
5. Deploy container

## 6. Terraform Infrastructure

- Branch `main` provisions resources using Terraform + Terraform Cloud
- Manages Azure Blob Storage and other cloud infrastructure
- Enables easier state management and reproducibility

## Project Structure (Overview)

```
FastAPI/           # FastAPI application
Scripts/           # Training, prediction, and upload scripts
models/            # Saved model & vectorizer
Terraform/         # Terraform code for cloud provisioning
Jenkinsfiles/      # Jenkins pipelines
Dockerfile         # Docker image for API
requirements.txt
Jupyter notebook   # Data exploration and initial training
```

## Future Enhancements

- Full integration tests with Azure storage
- Versioned model storage and rollback
- Monitoring & alerting for model performance
- Kubernetes-based scalable deployment
- CI/CD triggers for automated retraining on new data

## Local Setup

### Prerequisites

- Python 3.10+
- Docker
- Azure account (for Blob Storage)
- Terraform & Terraform Cloud (for infrastructure provisioning)
- Jenkins (optional, for CI/CD pipelines)

### Install Dependencies

```bash
git clone https://github.com/amalsboui/Sentiment-Analysis-MLOps.git
cd Sentiment-Analysis-MLOps
pip install --upgrade pip
pip install -r requirements.txt
```
