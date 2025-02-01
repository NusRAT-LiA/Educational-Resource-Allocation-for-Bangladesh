import pandas as pd
from fastapi import APIRouter

router = APIRouter()

df = pd.read_csv("data/education_data_clustered.csv")

@router.get("/resource_allocation/{division}")
def get_resource_recommendations(division: str):
    division_data = df[df["Division"] == division]

    if division_data.empty:
        return {"message": "No data available for this division"}

    avg_dropout = division_data["Dropout_Rate"].mean()
    avg_completion = division_data["Completion_Rate"].mean()
    avg_tsr = division_data["TSR"].mean()
    avg_infra_score = division_data["Infrastructure_Score"].mean()

    recommendations = []
    if avg_dropout > 20:
        recommendations.append("Invest in student retention programs")
    if avg_completion < 80:
        recommendations.append("Allocate more budget for learning materials")
    if avg_tsr < 30:
        recommendations.append("Hire additional teachers")
    if avg_infra_score < 10:
        recommendations.append("Improve infrastructure")

    return {
        "division": division,
        "average_dropout_rate": round(avg_dropout, 2),
        "average_completion_rate": round(avg_completion, 2),
        "average_tsr": round(avg_tsr, 2),
        "infrastructure_score": round(avg_infra_score, 2),
        "resource_allocation_recommendations": recommendations
    }
