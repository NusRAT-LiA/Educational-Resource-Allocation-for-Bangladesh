from fastapi import FastAPI
from app.routes import prediction_routes, cluster_routes, resource_routes

app = FastAPI()

app.include_router(prediction_routes.router, prefix="/api")
app.include_router(cluster_routes.router, prefix="/api")
app.include_router(resource_routes.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "ML Resource Allocation API"}
