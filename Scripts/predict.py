import pickle

#Load model and vectorizer
with open('./models/sentiment_classifier.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('./models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Example prediction
def predict_sentiment(text):
    vect = vectorizer.transform([text])
    return clf.predict(vect)[0]

# Test
sample = "Not much"
print("Sentiment:", predict_sentiment(sample))