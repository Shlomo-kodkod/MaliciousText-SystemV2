import os
from pathlib import Path


blacklist_path = os.getenv("BLACKLIST_PATH", "/app/data/weapons_blacklist.txt")
prv_topic1 = "preprocessed_tweets_antisemitic"
prv_topic0 = "preprocessed_tweets_not_antisemitic"
next_topic1 = "enriched_preprocessed_tweets_antisemitic"
next_topic0 = "enriched_preprocessed_tweets_not_antisemitic"
group_id = "enricher"