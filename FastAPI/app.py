from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from azure.storage.blob import BlobServiceClient

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "models"
MODEL_BLOB_NAME = "sentiment_classifier.pkl"
VECTORIZER_BLOB_NAME = "vectorizer.pkl"

def download_model(local_path="model.pkl"):
    blob_service = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(BLOB_NAME)
    
    #you can add local backup
    blob_data = blob_client.download_blob().readall()
    return pickle.load(BytesIO(blob_data))

# Load model and vectorizer directly from Azure
clf = load_blob_model(MODEL_BLOB_NAME)
vectorizer = load_blob_model(VECTORIZER_BLOB_NAME)

app = FastAPI(title="Sentiment Analysis API")

# Input schema
class Review(BaseModel):
    text: str

#Prediction endpoint
@app.post("/predict")
def predict_sentiment(review: Review):
    vect = vectorizer.transform([review.text])
    sentiment = clf.predict(vect)[0]
    return{"sentiment": sentiment}
    