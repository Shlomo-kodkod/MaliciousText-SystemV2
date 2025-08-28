import time
import logging
from services.dal import DAL
from services.retriever.app import config 
from services.kafka import producer


logger = logging.getLogger(__name__)

class Retrieval:
    def __init__(self):
        self.__dal = DAL(config.protocol, config.username, config.password, config.cluster)
        self.__producer = producer.Producer()
        self.__offset = 0

    def __get_newest_tweets(self, sort_by: str ="CreateDate", limit: int = 100):
        query = [
    { "$sort": { sort_by: -1 } },
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
    
    def __publish_tweet(self, tweet: list[dict], label: str = "antisemitic"):
        try:
            for record in tweet:
                if record.get(label) == 1:
                    self.__producer.publish_message(config.topic1, record)
                else:
                    self.__producer.publish_message(config.topic0, record)
                logger.info(f"Published {len(tweet)} tweets to Kafka by topic.")
        except Exception as e:
            logger.error(f"Failed to publish tweets: {e}")
    
    def run(self):
        while True:
            tweets = self.__get_newest_tweets()
            if tweets:
                self.__publish_tweet(tweets)
                time.sleep(60)
            else:
                logger.info("No new tweets to process.")
                break
