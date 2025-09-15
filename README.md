[![API Docker Image Version](https://img.shields.io/badge/sentimentapi-latest-blue?logo=docker)](https://hub.docker.com/repository/docker/hophopp/sentiment-api/tags)

# Sentiment Analysis MLOps Project
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Terraform Cloud](https://img.shields.io/badge/Terraform_Cloud-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Azure Blob Storage](https://img.shields.io/badge/Azure_Blob_Storage-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
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

#### Pipeline Stages:
1. Checkout repository
2. Run tests
3. Build Docker image (the image is built from FastAPI using the model already uploaded on Azure Blob)
4. Push Docker image to Docker Hub
5. Deploy container


## 6. Terraform Infrastructure

In the `main` branch, Terraform and Terraform Cloud are used to provision and manage cloud resources for the project. This setup provides several advantages:

- **Infrastructure as Code**: All Azure resources are defined declaratively, ensuring consistency and reproducibility.  
- **Terraform Cloud Workspace**: The project uses the workspace `sentiment-azure-storage` in the organization `hophopp_cc`, which manages the state file and enables collaboration.  
- **Automated Resource Creation**: Azure resources, such as storage accounts and blob containers, are automatically created with unique names to avoid conflicts.  
- **State Management**: Terraform Cloud tracks the state of resources, allowing easy updates and rollback if needed.

### Resources Provisioned

1. **Resource Group**: A container for all related Azure resources to simplify management.  
2. **Storage Account**: Provides persistent storage for trained models and datasets.  
3. **Blob Containers**:  
   - `models`: Stores trained model and vectorizer files.  
   - `datasets`: Stores the dataset. When a dataset is uploaded, the model is automatically downloaded through the pipeline for API usage.  


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
