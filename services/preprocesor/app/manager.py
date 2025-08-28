import logging
from services.preprocesor.app import config
from services.kafka.producer import Producer
from services.kafka import configurations
from services.utiles.cleaner import TextCleaner


logger = logging.getLogger(__name__)

class Manager:
    def __init__(self):
        self.producer = Producer()
        self.text_cleaner = TextCleaner()

    def run(self):
        """
        Consumes raw tweets from Kafka topics, cleans and preprocesses the text,
        and publishes the processed tweets.
        """
        event = configurations.get_consumer_events(config.prv_topic0, config.prv_topic1, group_id=config.group_id)
        for tweet in event:
            try:
                tweet_value = tweet.value
                if tweet_value is None:
                    logger.warning("Received tweet with None value.")
                    continue
                original_text = tweet_value.get('text', '')
                clean_text = self.text_cleaner.clean(original_text)
                tweet_value['clean_text'] = clean_text
                if tweet_value.get("label") == 1:
                    self.producer.publish_message(config.next_topic1, tweet_value)
                    logger.info("Published preprocessed antisemitic tweet to topic 1")
                else:
                    self.producer.publish_message(config.next_topic0, tweet_value)
                    logger.info("Published preprocessed non-antisemitic tweet to topic 0")
            except Exception as e:
                logger.error(f"Failed to process individual tweet: {e}")
                continue
    

