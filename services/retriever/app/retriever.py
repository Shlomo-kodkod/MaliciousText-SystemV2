import time
import logging
from services.utiles.dal import DAL
from services.retriever.app import config 
from services.kafka import producer


logger = logging.getLogger(__name__)

class Retrieval:
    def __init__(self):
        self.__dal = DAL(config.uri)
        self.__producer = producer.Producer()
        self.__offset = 0

    def __get_oldest_tweets(self, sort_by: str = "CreateDate", limit: int = 100):
        """
        Retrieve the newest tweets from the database.
        """
        query = [
            { "$sort": { sort_by: 1 } },
            { "$skip": self.__offset },
            { "$limit": limit },
            { "$project": { "_id": 0 } }]
        
        try:
            self.__dal.connect(config.db)
            data = self.__dal.read_collection(config.collection, query)
            self.__offset += limit
            self.__dal.disconnect()
            logger.info(f"Retrieved {len(data)} tweets from the database.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve tweets: {e}")
            return None
    
    def __publish_tweets(self, tweets: list, label: str = "Antisemitic"):
        """
        Publish tweets to appropriate Kafka topics.
        """
        try:
            for record in tweets:
                if record.get(label) == 1:
                    self.__producer.publish_message(config.topic1, record)
                else:
                    self.__producer.publish_message(config.topic0, record)
                logger.info(f"Published tweets to Kafka by topic.")
        except Exception as e:
            logger.error(f"Failed to publish tweets: {e}")
    
    def run(self):
        """
        retrieves new tweets from the database and publishes them to Kafka.
        """        
        while True:
            tweets = self.__get_oldest_tweets()
            if tweets:
                self.__publish_tweets(tweets)
            time.sleep(60)
            
