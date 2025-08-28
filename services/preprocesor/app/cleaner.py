from pydoc import text
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


class TextCleaner:
    def __init__(self,data:str):
        self.Data = data

    def removing_punctuation_marks(self):
        self.Data = self.Data.str.replace('[^\w\s]', '', regex=True)

    def removing_special_characters(self):
        self.Data = self.Data.str.replace('[^a-zA-Z0-9]', ' ', regex=True)

    def removing_unnecessary_whitespace(self):
        self.Data = self.Data.str.replace('\s+', ' ', regex=True).str.strip()

    @staticmethod
    def removing_stop_word(text):
        stop_words = set(stopwords.words('english'))
        x = text.split()
        x = [word for word in x if word not in stop_words]
        return ' '.join(x)

    def removing_stop_words(self):
        self.Data = self.Data.apply(TextCleaner.removing_stop_word)

    def convert_to_lowercase(self):
        self.Data = self.Data.str.lower()

    @staticmethod
    def row_lemmatize(text):
        x = text.split()
        lemmatizer = nltk.stem.WordNetLemmatizer()
        x = [lemmatizer.lemmatize(word) for word in x]
        return ' '.join(x)

    def lemmatize(self):
        self.Data = self.Data.apply(TextCleaner.row_lemmatize)
