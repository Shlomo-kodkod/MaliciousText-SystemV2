import logging
from services.kafka.producer import Producer
from services.kafka import configurations
from services.enricher.app import config
from services.enricher.app.enricher import Enricher

logger = logging.getLogger(__name__)

class Manager:
    def __init__(self):
        self.__producer = Producer()
        self.__enricher = Enricher()

    def run(self):
        """
        Consumes tweets from Kafka topics, enriches them, and publishes
        the enriched tweets by topics.
        """    
        event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
        
        for tweet in event:
            try:
                tweet_value = tweet.value
                processed_data = self.__enricher.processor(tweet_value, "clean_text")
                if processed_data.get("label") == 1:
                    self.__producer.publish_message(config.next_topic1, processed_data)
                    logger.info("Published enriched antisemitic tweet to topic 1")
                else:
                    self.__producer.publish_message(config.next_topic0, processed_data)
                    logger.info("Published enriched non-antisemitic tweet to topic 0")     
            except Exception as e:
                logger.error(f"Failed to process tweet: {e}")
                continue
        

