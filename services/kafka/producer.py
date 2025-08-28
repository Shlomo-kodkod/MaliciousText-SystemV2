import logging
from services.kafka.configurations import get_producer_config

logger = logging.getLogger(__name__)

class Producer:
    def __init__(self):
        self.__producer = get_producer_config()

    def publish_message(self, topic: str, message):
        """
        Publish message to the topic which is received as a parameter.
        """
        logging.info(f"Publish json messages to: {str(topic)}")
        self.__producer.send(topic, message)
    

    def publish_messages(self, topic, message: list):
        """
        Publish list of messages to the topic which is received as a parameter.
        """
        for i in message:
            self.publish_message(topic, i)    

