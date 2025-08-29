import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datefinder
import logging
from services.enricher.app import config
from services.utils.cleaner import TextCleaner


logger = logging.getLogger(__name__)


class Enricher:
    def __init__(self):
        self.__cleaner = TextCleaner()
        self.__weapons = None

    @staticmethod
    def calculate_sentiment_score(text: str) -> str:
        """
        Analyzes the sentiment of a given text string and returns a sentiment score.
        """
        try:
            score = SentimentIntensityAnalyzer().polarity_scores(text)
            result = score["compound"]
            logger.info(f"Successfully calculated sentiment score: {result}")
            if result >= 0.05: return "positive"
            elif result <= -0.05: return "negative"
            else: return "neutral"
        except Exception as e:
            logger.error(f"Failed to calculate sentiment score: {e}")
            return 0.0

    def load_blacklist(self, file_path: str):
        """
        Load a blacklist of weapons from data file and return set of weapons.

        """
        try:
            with open(file_path, 'r') as file:
                blacklist = list(file.read().splitlines())
            self.__weapons = [self.__cleaner.clean(i) for i in blacklist]
            logger.info("Blacklist loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load blacklist: {e}")
            raise e

    def find_weapons(self, text: str, weapons: list) -> list:
        """
        Find weapons in the given text using the provided set of weapons.
        """
        found_weapons = [w for w in weapons if w in text]
        return found_weapons 
        
    @staticmethod
    def is_date(text: str) -> bool:
        """
        Checks if the text is a date.
        """
        try:
            parsed_date = parse(text, fuzzy=True)
            return True
        except Exception:
            return False
        

    @staticmethod
    def find_latest_date(text: str):
        """
        Finds the latest date in the text, if any.
        """
        matches = list(datefinder.find_dates(text, index=False))
        if matches:
            logger.info("Found latest date")
            return max(matches)
        else:
            logger.info("No dates found in text")
            return " "

    def processor(self, data: dict, field: str = "text") -> dict:
        """
        Process the text, and add new fields. 
        """
        try:
            if not isinstance(self.__weapons, list):
                self.load_blacklist(config.blacklist_path)
            
            text_content = data.get(field, "")
            data["sentiment"] = Enricher.calculate_sentiment_score(text_content)
            data["weapons_detected"] = self.find_weapons(text_content, self.__weapons)
            data["relevant_timestamp"] = Enricher.find_latest_date(text_content)
            logger.info("Successfully processed and enriched data")
            return data
        except Exception as e:
            logger.error(f"Failed to process and enrich data: {e}")
            return data 