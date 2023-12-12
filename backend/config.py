
import os

# environment variables for MongoDB credentials
MONGO_DB = os.getenv('MONGODB_DATABASE', 'planet_djanet')
MONGO_HOST = os.getenv('MONGODB_HOSTNAME', 'localhost')
MONGO_PASSWORD = os.getenv('MONGODB_PASSWORD', 'rootpwd')
MONGO_PORT = os.getenv('MONGO_PORT', '27017')
MONGO_USER = os.getenv('MONGODB_USERNAME', 'root')