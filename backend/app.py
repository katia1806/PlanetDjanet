from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import os

app = FastAPI()

# environment variables for MongoDB credentials
MONGO_USER = os.getenv('MONGO_USER', 'root')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'rootpwd')
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', '27017')
MONGO_DB = os.getenv('MONGO_DB', 'planet_djanet')

# setup MongoDB Client
client = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
)
db = client[MONGO_DB]

@app.get("/data/{file_name}")
async def get_data(file_name: str):
    """Get data from the specified file/collection in MongoDB."""
    # # Here, we use file_name to decide the collection we're querying
    # if file_name.endswith('.json'):
    #     collection_name = file_name[:-5]  
    # elif file_name.endswith('.csv'):
    #     collection_name = file_name[:-4] 
    # else:
    #     raise HTTPException(status_code=400, detail="Invalid file name extension")

    collection = db["posts_1"]
    
    # Perform the query (retrieving all documents in the collection)
    try:
        data = list(collection.find({}))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"file_name": file_name, "data": data}