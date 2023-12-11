from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List, Dict
import os

app = FastAPI()

# Environment variables for MongoDB credentials
MONGO_USER = os.getenv('MONGO_USER', 'default_user')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'default_password')
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', '27017')
MONGO_DB = os.getenv('MONGO_DB', 'planet_djanet')

FACEBOOK_DATA = [
    "all_content", 
    "couverture_fb", 
    "likes_fb"
]

INSTAGRAM_DATA = [
    "all_content",  
    "couverture_insta", 
    "visitors_insta", 
    "likes_gender_age", 
    "followers_insta_gender_age", 
    "following",
    "followers"
]

META_DATA = [
    "posts", 
    "posts_1", 
    "pub", 
    "likes_city"
]

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