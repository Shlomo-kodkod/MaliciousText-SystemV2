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
        try:
            event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
            for tweet in event:
                processed_data = self.__enricher.processor(tweet.value, "clean_text")
                if processed_data.get("antisemitic"):
                    self.__producer.publish_message(config.next_topic1, processed_data)
                else:
                    self.__producer.publish_message(config.next_topic0, processed_data)
                logger.info(f"Published {len(tweet)} tweets to Kafka by topic.")
        except Exception as e:
            logger.error(f"Failed to publish tweets: {e}")


