from pymongo import MongoClient
from config import (
    MONGO_DB,
    MONGO_HOST,
    MONGO_PASSWORD,
    MONGO_PORT,
    MONGO_USER,
)

class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(
            f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
        )
        self.db = self.client[MONGO_DB]

    def get_collection(self, collection_name:str) -> list:
        """Get the specified collection from the database
        Args:
            collection_name: Name of the collection to retrieve
        Returns:
            The specified collection
        """
        # get the collection
        collection = self.db[collection_name]
        
        # transform the _id field into a string
        data = list(collection.find({}))
        for item in data:
            item["_id"] = str(item["_id"])  
            
        return data

    def close(self):
        """Close the MongoDB connection"""
        self.client.close()
        