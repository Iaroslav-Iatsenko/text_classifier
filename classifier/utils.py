import joblib
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path

# Load artifacts once
ARTIFACTS_DIR = Path(__file__).resolve().parent.parent
artifacts = joblib.load(ARTIFACTS_DIR / "model_files/artifacts.joblib")
MODEL_NAME = artifacts["model_name"]
LABEL_ENCODER = artifacts["label_encoder"]
KNN = artifacts["knn"]

# Lazy-load the transformer model
_model = None
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def forecast_class(text):
    model = get_model()
    embedding = model.encode(text)
    pred_encoded = KNN.predict([embedding])
    pred_label = LABEL_ENCODER.inverse_transform(pred_encoded)
    return pred_label[0]