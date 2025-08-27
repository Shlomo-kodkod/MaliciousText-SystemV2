from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)


class DAL:
    def __init__(self, protocol: str, username: str, password: str, cluster: str, db: str):
        self.__protocol = protocol
        self.__username = username
        self.__password = password
        self.__cluster = cluster 
        self.__client = None
        self.__db = db

    def connect(self, ):
        """
        Connect to the mongo database.
        """
        try:
            uri = f"{self.__protocol}://{self.__username}:{self.__password}@{self.__cluster}.mongodb.net/"
            self.__client = MongoClient(uri)
            self.__db = self.__client[self.__db]
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
        
    def create_document(self, collection_name, data: dict):
        """
        Create a soldier document and insert into the mongodb collection.
        """
        try:
            collection = self.__db[collection_name]
            result = collection.insert_one(data)
            logger.info(f"Data inserted successfully.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to insert data: {e}")
            raise e
        
   