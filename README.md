# Sentiment Analysis MLOps Project (Local Branch)

## Overview

This branch provides a **simplified local setup** for the Sentiment Analysis project.  
Unlike the `main` branch (which uses Azure Blob Storage and Terraform for infrastructure), this version:

- Stores models directly in the **GitHub repo** (`/models` folder)
- Includes **unit tests** (for the model) and **API tests** (for FastAPI)
- Uses a **single Jenkins pipeline** for testing, building, and pushing the Docker image

This setup is ideal for local development, testing, and experimentation.

---

## Workflow

1. **Dataset & Model Training**
   - Dataset: [IMDB Movie Reviews (50,000 reviews)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)  
   - Sampled 5,000 reviews for training and rapid iteration  
   - Preprocessing with TF-IDF + classifier  
   - Model and vectorizer are saved into the `models/` folder (tracked in GitHub)

2. **FastAPI Application**
   - `app.py` serves predictions using the locally stored model  
   - Tested with `pytest` for both the model and the API endpoints

3. **Dockerization**
   - FastAPI app is containerized via `Dockerfile`
   - Image pushed to Docker Hub:  
     👉 [hophopp/sentiment-api](https://hub.docker.com/repository/docker/hophopp/sentiment-api/general)

4. **Jenkins Pipeline (Single)**
   - **Checkout repo**
   - **Run tests** (`pytest tests/`)
   - **Build Docker image**
   - **Push image to Docker Hub**
   - **Deploy container** (runs on port 8088 by default)

---

## Project Structure (Local)

Sentiment-Analysis-MLOps/
│
├── FastAPI/             # FastAPI application
├── models/              # Trained model + vectorizer (stored in GitHub)
├── Scripts/             # Training and prediction scripts
├── tests/               # Unit tests (model + API)
├── Jenkinsfile          # Jenkins pipeline (test + build + deploy)
├── Dockerfile           # Docker image definition
├── requirements.txt     # Dependencies
└── Jupyter notebook     # Initial experimentation


