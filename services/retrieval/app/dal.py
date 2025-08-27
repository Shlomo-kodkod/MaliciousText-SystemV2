from pymongo import MongoClient
import pandas as pd
import logging
from app import config

logger = logging.getLogger(__name__)


class DAL:
    def __init__(self):
        self.__client = None
        self.__db = None
        self.__df = None

    def connect(self):
        """
        Connect to the mongo atlas database.
        """
        try:
            uri = f"mongodb+srv://{config.username}:{config.password}@{config.cluster}.mongodb.net/"
            self.__client = MongoClient(uri)
            self.__db = self.__client[config.db]
            logger.info(f"Connected to mongodb.")
        except Exception as e:
            logger.error(f"Failed to connect to mongodb: {e}")
            raise e

    def disconnect(self):
        """
        Disconnect from the mongo atlas database.
        """
        if self.__client is not None:
            self.__client.close()
            logger.info("Database connection closed.")

    def read_collection(self, collection_name=config.collection):
        """""
        Read a collection from the mongo atlas database.
        """
        try:
            collection = self.__db[collection_name]
            data = list(collection.find({}, {"_id": 0}))
            logger.info(f"Data loaded successfully.")
            self.__df = pd.DataFrame(data)
        except Exception as e:
            logger.error(f"Failed to retrieve collection: {e}")
            raise e

    @property
    def get_df(self) -> pd.DataFrame:
        """
        Get the dataframe containing the collection data.
        """
        return self.__df
