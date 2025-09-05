from azure.storage.blob import BlobServiceClient
import os

# Setup
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "models"

MODEL_LOCAL_PATH = "models/sentiment_classifier.pkl"
VECTORIZER_LOCAL_PATH = "models/vectorizer.pkl"

# always overwrite "latest" model
MODEL_BLOB_NAME = "sentiment_classifier.pkl"
VECTORIZER_BLOB_NAME = "vectorizer.pkl"

def upload_blob(local_path, blob_name):
    blob_service = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(blob_name)

    with open(local_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded {blob_name} to {CONTAINER_NAME}")

# Upload both model and vectorizer
upload_blob(MODEL_LOCAL_PATH, MODEL_BLOB_NAME)
upload_blob(VECTORIZER_LOCAL_PATH, VECTORIZER_BLOB_NAME)
