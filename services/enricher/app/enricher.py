import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dateutil.parser import parse
import logging
import datetime
from services.enricher.app import config



logger =  logging.getLogger(__name__)



class Enricher:
    @staticmethod
    def calculate_sentiment_score(text: str) -> str:
        """
        Analyzes the sentiment of a given text string and returns a sentiment score.
        """
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        result = score["compound"]
        logger.info(f"Successfully calculated sentiment score.")
        return result
    

    @staticmethod
    def load_blacklist(file_path: str) -> list:
        """
        Load a blacklist of weapons from data and return set of weapons.
        """
        try:
            with open(file_path, 'r') as file:
                blacklist = list(file.read().splitlines())
            logger.info("Blacklist loaded successfully.")
            return blacklist
        except Exception as e:
            logger.error(f"Failed to load blacklist: {e}")
            raise e

    @staticmethod
    def find_weapons(text: str, weapons: list) -> list:
        """
        Find weapons in the given text using the provided set of weapons.
        """
        found_weapons = [weapon for weapon in weapons if weapon in text]
        return found_weapons if found_weapons else None

    @staticmethod
    def weapons_detector(tweet: dict, field: str = "text") -> dict:
        """
        Add a new field to the DataFrame with detected weapons for each row.
        """
        try:
            weapons = Enricher.load_blacklist(config.blacklist_path)
            tweet['weapons_detected'] = Enricher.find_weapons(tweet[field], weapons)
            logger.info("Successfully detected weapons.")
        except Exception as e:
            logger.error(f"Failed to detect weapons: {e}")
        return tweet
    
    @staticmethod
    def is_date(string, fuzzy=False):
        """
        Return whether the string can be interpreted as a date.
        """
        try: 
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def find_latest_date(text: str):
        """

        """
        split_text = text.split()
        return  max([datetime.datetime.strptime(i, '%Y-%m-%d') for i in split_text if Enricher.is_date(i)])
    
    def processor(self, data: dict, field: str = "text") -> dict:
        """
        """
        weapons = Enricher.load_blacklist(config.blacklist_path)
        data["sentiment"] = Enricher.calculate_sentiment_score(data[field])
        data["weapons_detected"] = Enricher.find_weapons(data[field], weapons)
        data["relevant_timestamp"] = Enricher.find_latest_date(data[field])
        return data
    