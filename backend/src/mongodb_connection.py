# Standard imports
import os

# Installed imports
from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self):
        # Constants
        MONGO_DB = os.getenv('MONGODB_DATABASE', 'planet_djanet')
        MONGO_HOST = os.getenv('MONGODB_HOSTNAME', 'localhost')
        MONGO_PASSWORD = os.getenv('MONGODB_PASSWORD', 'rootpwd')
        MONGO_PORT = os.getenv('MONGO_PORT', '27017')
        MONGO_USER = os.getenv('MONGODB_USERNAME', 'root')

        self.client = MongoClient(
            f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
        )
        self.db = self.client[MONGO_DB]

    def get_collection(self, collection_name: str) -> list:
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
