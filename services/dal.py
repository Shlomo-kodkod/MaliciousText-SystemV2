from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)


class DAL:
    def __init__(self):
        self.__client = None
        self.__db = None

    def connect(self, protocol: str, username: str, password: str, cluster: str):
        """
        Connect to the mongo database.
        """
        try:
            uri = f"{protocol}://{username}:{password}@{cluster}.mongodb.net/"
            self.__client = MongoClient(uri)
            self.__db = self.__client[config.db]
            logger.info(f"Connected to mongodb.")
        except Exception as e:
            logger.error(f"Failed to connect to mongodb: {e}")
            raise e

    def disconnect(self):
        """
        Disconnect from the mongo database.
        """
        if self.__client is not None:
            self.__client.close()
            logger.info("Database connection closed.")

    def read_collection(self, collection_name, query):
        """""
        Read a collection from the mongo database.
        """
        try:
            collection = self.__db[collection_name]
            data = list(collection.find(query))
            logger.info(f"Data loaded successfully.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve collection: {e}")
            raise e
        
    def create_document(self, data: dict):
        """
        Create a soldier document and insert into the mongodb collection.
        """
        try:
            collection = self.__db[config.collection]
            result = collection.insert_one(data)
            logger.info(f"Data inserted successfully.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to insert data: {e}")
            raise e
        
   