import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pickle
import os


#load data
os.makedirs('./models', exist_ok=True)
df = pd.read_csv("IMDB_DATASET.csv").sample(n=5000, random_state=42)

# split data
train_texts, test_texts, train_y, test_y = train_test_split(
    df['review'], df['sentiment'], test_size=0.33, random_state=81
)

#vectorize
vectorizer = TfidfVectorizer()
train_x_vectors = vectorizer.fit_transform(train_texts)

#Train model
clf = SVC(kernel='linear')
clf.fit(train_x_vectors, train_y)

#Save model and vectorizer
with open('./models/sentiment_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)
with open('./models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Training complete. Model and vectorizer saved.")