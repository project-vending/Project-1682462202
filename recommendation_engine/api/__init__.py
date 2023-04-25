python
from fastapi import FastAPI
from src.recommender import Recommender

app = FastAPI()

# Initialize the recommender object
recommender = Recommender()

# Define an API endpoint for getting recommendations
@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommender.get_recommendations(user_id)
    return {"user_id": user_id, "recommendations": recommendations}
