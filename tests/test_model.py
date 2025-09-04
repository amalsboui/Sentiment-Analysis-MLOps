import pickle
import os
import pytest
from sklearn.exceptions import NotFittedError

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/sentiment_classifier.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "../models/vectorizer.pkl")


@pytest.fixture
def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

@pytest.fixture
def load_vectorizer():
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    return vectorizer


def test_model_exists(load_model):
    """Test that the model file loads correctly."""
    assert load_model is not None

def test_vectorizer_exists(load_vectorizer):
    """Test that the vectorizer file loads correctly."""
    assert load_vectorizer is not None

def test_vectorizer_transform(load_vectorizer):
    """Test that vectorizer can transform text."""
    sample_text = ["I love this movie!"]
    transformed = load_vectorizer.transform(sample_text)
    assert transformed.shape[0] == 1
    assert transformed.shape[1] > 0  

def test_model_predict(load_model, load_vectorizer):
    """Test that model can make a prediction."""
    sample_text = ["This movie was terrible."]
    X = load_vectorizer.transform(sample_text)
    try:
        pred = load_model.predict(X)
        assert len(pred) == 1
        assert pred[0] in ["positive", "negative"]
    except NotFittedError:
        pytest.fail("Model is not fitted yet")
