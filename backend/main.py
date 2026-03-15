from fastapi import FastAPI

app = FastAPI(
    title="StayPilot API",
    description="API for StayPilot rental recommendations",
    version="1.0"
)

@app.get("/")
def read_root():
    return {"message": "StayPilot API is running"}

@app.get("/recommendations")
def get_recommendations(city: str):
    return {
        "city": city,
        "recommendations": [
            {
                "name": "Downtown Loft",
                "price_per_night": 150,
                "rating": 4.8
            },
            {
                "name": "Riverfront Apartment",
                "price_per_night": 120,
                "rating": 4.6
            },
            {
                "name": "City Center Studio",
                "price_per_night": 100,
                "rating": 4.5
            }
        ]
    }
