from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)


class DAL:
    def __init__(self, uri):
        self.__uri = uri
        self.__client = None
        self.__db = None

    def connect(self, db: str):
        """
        Connect to the mongo database.
        """
        try:
            uri = self.__uri
            self.__client = MongoClient(uri)
            self.__db = self.__client[db]
            logger.info(f"Connected to MongoDB database: {db}")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise e

    def disconnect(self):
        """
        Disconnect from the mongo database.
        """
        if self.__client is not None:
            self.__client.close()
            logger.info("Database connection closed.")

    def read_collection(self, collection_name: str, query: list = None):
        """
        Read a collection from the MongoDB database.
        """
        if query is None:
            query = []
            
        try:
            collection = self.__db[collection_name]
            data = list(collection.aggregate(query))
            logger.info(f"Data loaded successfully.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve collection : {e}")
            raise e
        
    def create_document(self, collection_name: str, data: dict):
        """
        Create a document and insert into the mongodb collection.
        """
        try:
            collection = self.__db[collection_name]
            result = collection.insert_one(data)
            logger.info(f"Data inserted successfully.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to insert data: {e}")
            raise e
        
