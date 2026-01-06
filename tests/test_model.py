import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

def test_model_load():
    model = joblib.load("diabetes_model.pkl")
    assert model is not None
    assert hasattr(model, "predict")

def test_model_prediction():
    model = joblib.load("diabetes_model.pkl")
    sample = np.array([[2, 130, 70, 28.5, 45]])
    prediction = model.predict(sample)
    assert prediction.shape == (1,)
    assert prediction[0] in [0, 1]
