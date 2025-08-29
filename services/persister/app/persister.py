import logging
from services.kafka.producer import Producer
from services.kafka import configurations
from services.persister.app import config
from services.utils.dal import DAL


logger = logging.getLogger(__name__)

class Persister:
    def __init__(self):
        self.__dal = DAL(config.uri)

    def run(self):
        """
        Consumes enriched tweets from Kafka topics and saves them to MongoDB
        collections by topics.
        """
        self.__dal.connect(config.db)
        event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
            
        for tweet in event:
            try:
                tweet_value = tweet.value
                if tweet_value is None:
                    logger.error("Received tweet with None value")
                    continue 
                if tweet_value.get("Antisemitic") == 1:
                    self.__dal.create_document(config.collection_antisemitic, tweet_value)
                    logger.info("Saved antisemitic tweet to antisemitic collection")
                else:
                    self.__dal.create_document(config.collection_not_antisemitic, tweet_value)
                    logger.info("Saved non-antisemitic tweet to non-antisemitic collection")      
            except Exception as e:
                logger.error(f"Failed to persist tweet: {e}")
                continue
        self.__dal.disconnect()
                
       