import joblib
import numpy as np
from fastapi import APIRouter
from app.services.recommender import generate_recommendations

router = APIRouter()

# Load models
dropout_model = joblib.load("data/models/dropout_model.pkl")
completion_model = joblib.load("data/models/completion_model.pkl")
tsr_model = joblib.load("data/models/tsr_model.pkl")

@router.post("/predict")
def predict_school_performance(total_students: int, female_students: int, disabled_students: int, teachers: int, budget: float, pass_rate: float, internet_access: int):
    input_data = np.array([[total_students, female_students, disabled_students, teachers, budget, pass_rate, internet_access]])
    
    predicted_dropout = dropout_model.predict(input_data)[0]
    predicted_completion = completion_model.predict(input_data)[0]
    predicted_tsr = tsr_model.predict(input_data)[0]

    recommendations = generate_recommendations(predicted_dropout, predicted_completion, predicted_tsr)

    return {
        "predicted_dropout_rate": round(predicted_dropout, 2),
        "predicted_completion_rate": round(predicted_completion, 2),
        "predicted_tsr": round(predicted_tsr, 2),
        "recommendations": recommendations
    }
