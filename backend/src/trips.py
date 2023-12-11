from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()

@app.post("/save_reservation")
async def save_reservation(reservation: Reservation):
    try:
        result = collection.insert_one(reservation.dict())
        return {"message": "Reservation saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))