import logging
from services.kafka.producer import Producer
from services.kafka import configurations
from services.persister.app import config
from services.dal import DAL


logger =  logging.getLogger(__name__)



class Presister:
    def __init__(self):
        self.__dal = DAL()

    def run(self):
        try:
            event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
            for tweet in event:
                if event.value.get("antisemitic"):
                    self.__dal.create_document(config.collection_antisemitic, tweet.value)
                else:
                    self.__dal.create_document(config.collection_not_antisemitic, tweet.value)
                logger.info(f"Published {len(tweet)} tweets to mongo by topic.")
        except Exception as e:
            logger.error(f"Failed to publish tweets: {e}")