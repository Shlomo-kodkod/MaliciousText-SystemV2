import os

protocol=os.getenv("MONGO_PROTOCOL", "mongodb+srv")
username=os.getenv("MONGO_INITDB_ROOT_USERNAME", "IRGC_NEW")
password=os.getenv("MONGO_INITDB_ROOT_PASSWORD", "iran135")
cluster = os.getenv("MONGO_INITDB_CLUSTER", "cluster0.6ycjkak")
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection = os.getenv("MONGO_COLLECTION", "tweets")
topic1 = "raw_tweets_antisemitic"
topic0 = "raw_tweets_not_antisemitic"
