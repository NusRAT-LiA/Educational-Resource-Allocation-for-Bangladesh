import pandas as pd
from fastapi import APIRouter

router = APIRouter()

df = pd.read_csv("/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/education_data_clustered.csv")

@router.get("/cluster")
def get_school_clusters():
    cluster_summary = df.groupby("Cluster").agg({
        "Infrastructure_Score": "mean",
        "Dropout_Rate": "mean",
        "Completion_Rate": "mean",
        "TSR": "mean"
    }).reset_index()
    
    return {"cluster_summary": cluster_summary.to_dict(orient="records")}
