import os 


protocol=os.getenv("MONGO_PROTOCOL", "mongodb")
host=os.getenv("MONGO_HOST", "mongodb-community-server")
port=int(os.getenv("MONGO_PORT", 27017))
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection_antisemitic = os.getenv("MONGO_COLLECTION_ANTISEMITIC", "tweets_antisemitic")
collection_not_antisemitic = os.getenv("MONGO_COLLECTION_NOT_ANTISEMITIC", "tweets_not_antisemitic")
uri=f"{protocol}://{host}:{port}/"