from fastapi import FastAPI
from pydantic import BaseModel
import pickle


with open('../models/sentiment_classifier.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('../models/vectorizer.pkl', 'rb') as f:
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