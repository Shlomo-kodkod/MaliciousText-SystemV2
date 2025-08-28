
from kafka import KafkaProducer,KafkaConsumer
import json
import logging

logger = logging.getLogger(__name__)

def get_producer_config():
    """
    Create a producer object and return it.
    """
    try:
        logger.info("Creating Kafka producer...")
        producer = KafkaProducer(
            bootstrap_servers=['broker:9092'],
            value_serializer=lambda x: json.dumps(x, default=lambda x: str(x)).encode('utf-8'))
        logger.info("Kafka producer created successfully")
        return producer
    except Exception as e:
        logger.error(f"Failed to create Kafka producer: {e}")
        raise e


def get_consumer_events(*topics, group_id: str):
    """
    Create a consumer object and return it.
    """
    try:
        logger.info(f"Creating Kafka consumer for topics: {topics}, group: {group_id}")
        consumer = KafkaConsumer(
            *topics,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=['broker:9092'],
            auto_offset_reset='earliest')
        logger.info("Kafka consumer created successfully")
        return consumer
    except Exception as e:
        logger.error(f"Failed to create Kafka consumer: {e}")
        raise e




