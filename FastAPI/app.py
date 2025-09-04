from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), '../models/sentiment_classifier.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../models/vectorizer.pkl')

with open(model_path, 'rb') as f:
    clf = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

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