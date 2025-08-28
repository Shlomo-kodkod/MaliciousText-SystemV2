import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dateutil.parser import parse
import logging
import datetime
from services.enricher.app import config
from services.utiles.cleaner import TextCleaner


logger =  logging.getLogger(__name__)



class Enricher:
    def __init__(self):
        self.__cleaner = TextCleaner()
        self.__weapons = None

    @staticmethod
    def calculate_sentiment_score(text: str) -> str:
        """
        Analyzes the sentiment of a given text string and returns a sentiment score.
        """
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        result = score["compound"]
        logger.info(f"Successfully calculated sentiment score.")
        return result
    

    def load_blacklist(self, file_path: str):
        """
        Load a blacklist of weapons from data and return set of weapons.
        """
        try:
            with open(file_path, 'r') as file:
                blacklist = list(file.read().splitlines())
            self.__weapons = [self.__cleaner.clean(i) for i in blacklist]
            logger.info("Blacklist loaded successfully.")
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

    def weapons_detector(self, tweet: dict, field: str = "text") -> dict:
        """
        Add a new field to the DataFrame with detected weapons for each row.
        """
        try:
            if not self.__weapons:
                self.load_blacklist(config.blacklist_path)
            tweet['weapons_detected'] = Enricher.find_weapons(tweet[field], self.__weapons)
            logger.info("Successfully detected weapons.")
        except Exception as e:
            logger.error(f"Failed to detect weapons: {e}")
        return tweet
    

    @staticmethod
    def find_latest_date(text: str):
        """
        Finds the latest date in the text, if any.
        """
        split_text = text.split()
        dates = []

        try:
            date = [parse(word, fuzzy=False) for word in split_text]
        except Exception as e:
            logger.error(f"Error: {e}")
              

        return max(dates) if dates else ""

    def processor(self, data: dict, field: str = "text") -> dict:
        """
        Process the text, and add new fields. 
        """
        self.load_blacklist(config.blacklist_path)
        data["sentiment"] = Enricher.calculate_sentiment_score(data[field])
        data["weapons_detected"] = Enricher.find_weapons(data[field], self.__weapons)
        data["relevant_timestamp"] = Enricher.find_latest_date(data[field])
        return data
    