from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List, Dict
from config import (META_DATA, FACEBOOK_DATA, INSTAGRAM_DATA, MONGO_DB, MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USER)
from pydantic import BaseModel
app = FastAPI()

from pydantic import BaseModel

class Reservation(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    number_of_tickets: int
    group_of: list[str]

    
# Setup MongoDB Client
client = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
)
db = client[MONGO_DB]

@app.get("/{page_name}")
async def get_data(page_name: str):
    """Retrieve data by page_name from the backend."""
    data = {} 
    try:
        if page_name == "facebook":
            for collection_name in FACEBOOK_DATA:
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
        elif page_name == "instagram":
            for collection_name in INSTAGRAM_DATA:
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
        elif page_name == "meta":
            for collection_name in META_DATA:
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
        else: pass

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data


@app.post("/save_reservation")
async def save_reservation(reservation: Reservation):
    collection = db[reservation]  
    try:
        result = collection.insert_one(reservation.dict())
        return {"message": "Reservation saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))