
from kafka import KafkaProducer,KafkaConsumer
import json
import logging


def get_producer_config():
    """
    Create a producer object and return it.
    """
    logging.info("Creating producer object ..")
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             json.dumps(x, default= lambda x : str(x)).encode('utf-8'))
    return producer


def get_consumer_events(*topic, group_id):
    """
    Create a consumer object and return it.
    """
    logging.info("Creating Consumer Object ..")
    consumer = KafkaConsumer(*topic,
                             group_id=group_id,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)
    return consumer




