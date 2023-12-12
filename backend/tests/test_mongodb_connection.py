import unittest
from backend.src.mongodb_connection import MongoDBConnection


class TestMongoDBConnection(unittest.TestCase):
    def setUp(self):
        """Set up the MongoDB connection"""

        self.mongo_connection = MongoDBConnection()

    def test_get_collection(self):
        """Test that we can get a collection from the database"""
        collection = self.mongo_connection.get_collection('following')
        self.assertIsNotNone(collection)

    def tearDown(self):
        """close the MongoDB connection"""
        self.mongo_connection.close()


if __name__ == '__main__':
    unittest.main()
