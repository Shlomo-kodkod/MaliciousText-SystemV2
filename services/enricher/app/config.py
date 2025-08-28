import os
from pathlib import Path



blacklist_path = Path('config.py').resolve().parent.parent.parent / 'data' / 'weapon_list.txt'
topic1 = "preprocessed_tweets_antisemitic"
topic0 = "preprocessed_tweets_not_antisemitic"