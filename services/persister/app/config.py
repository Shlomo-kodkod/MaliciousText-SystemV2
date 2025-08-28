import os



protocol=os.getenv("MONGO_PROTOCOL", "mongodb")
host=os.getenv("MONGO_HOST", "mongodb-community-server")
port=int(os.getenv("MONGO_PORT", 27017))
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection_antisemitic = os.getenv("MONGO_COLLECTION", "tweets_antisemitic")
collection_not_antisemitic = os.getenv("MONGO_COLLECTION", "tweets_not_antisemitic")
prv_topic1 = "enriched_preprocessed_tweets_antisemitic"
prv_topic0 = "enriched_preprocessed_tweets_not_antisemitic"
group_id = "persister"
uri=f"{protocol}://{host}:{port}/"