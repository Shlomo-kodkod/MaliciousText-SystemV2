import logging
from services.preprocesor.app import config
from services.kafka.producer import Producer
from services.kafka import configurations
from services.utiles.cleaner import TextCleaner



logger =  logging.getLogger(__name__)

class Manager:
    def __init__(self):
        self.producer = Producer()
        self.text_cleaner = TextCleaner()


    def run(self):
        try:
            event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
            for tweet in event:
                clean_text = self.text_cleaner.clean(tweet.value['text'])
                tweet.value['clean_text'] = clean_text
                if clean_text.get("antisemitic"):
                    self.producer.publish_message(config.next_topic1, tweet.value)
                else:
                    self.producer.publish_message(config.next_topic0, tweet.value)
                logger.info(f"Published {len(tweet)} tweets to Kafka by topic.")
        except Exception as e:
            logger.error(f"Failed to process tweets: {e}")





