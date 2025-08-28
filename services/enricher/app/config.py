import os
from pathlib import Path


blacklist_path = Path(__file__).resolve().parents[3] / 'data' / 'weapon_list.txt'

# blacklist_path = Path(__file__).resolve().parent.parent.parent / 'data' / 'weapon_list.txt'
prv_topic1 = "preprocessed_tweets_antisemitic"
prv_topic0 = "preprocessed_tweets_not_antisemitic"
next_topic1 = "enriched_preprocessed_tweets_antisemitic"
next_topic0 = "enriched_preprocessed_tweets_not_antisemitic"
group_id = "enricher"