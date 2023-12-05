from pymongo import MongoClient

def connect_to_db():
    client = MongoClient("your_mongodb_uri")  # Replace with your MongoDB URI
    db = client.your_database_name  # Replace with your database name
    return db

def save_reservation(data):
    db = connect_to_db()
    reservations = db.reservations
    reservations.insert_one(data)
