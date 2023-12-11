import os

# Environment variables for MongoDB credentials
MONGO_USER = os.getenv('MONGO_USER', 'default_user')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'default_password')
MONGO_HOST = os.getenv('MONGODB_HOSTNAME', 'localhost')
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