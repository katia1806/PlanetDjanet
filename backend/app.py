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

@app.get("/index/1")
async def test():
    return {"message": "Hello World"}

# Setup MongoDB Client
try : 
    client = MongoClient(
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
    )
    print(f"Connected to MongoDB at {MONGO_HOST}:{MONGO_PORT}")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

db = client[MONGO_DB]

@app.get("/{page_name}")
async def get_data(page_name: str):
    """Retrieve data by page_name from the backend."""
    data = {} 
    try:
        print(f"Retrieving data for page: {page_name}")
        if page_name == "facebook":
            for collection_name in FACEBOOK_DATA:
                print(f"Fetching data from collection: {collection_name}")
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
                print(f"Data from {collection_name}: {data[collection_name]}")
        elif page_name == "instagram":
            for collection_name in INSTAGRAM_DATA:
                print(f"Fetching data from collection: {collection_name}")
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
                print(f"Data from {collection_name}: {data[collection_name]}")
        elif page_name == "meta":
            for collection_name in META_DATA:
                print(f"Fetching data from collection: {collection_name}")
                data[collection_name] = list(db[collection_name].find({}, {"_id": 0}))
                print(f"Data from {collection_name}: {data[collection_name]}")
        else:
            print(f"No data found for page: {page_name}")
            pass

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return data


@app.post("/save_reservation")
async def save_reservation(reservation: Reservation):
    try:
        print(f"Saving reservation: {reservation.dict()}")
        collection = db['reservations']  # Assuming you have a 'reservations' collection
        result = collection.insert_one(reservation.dict())
        print(f"Reservation saved with ID: {result.inserted_id}")
        return {"message": "Reservation saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        print(f"Failed to save reservation: {e}")
        raise HTTPException(status_code=500, detail=str(e))