import re
from pydoc import text
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


class TextCleaner:
    def __init__(self,data:str):
        self.Data = data


    def removing_punctuation_marks(self):
        self.Data = re.sub(r"[^\w\s]", "", self.Data)
       
    def removing_special_characters(self):
        self.Data = re.sub(r"[^a-zA-Z0-9\s]", "", self.Data)

    def removing_unnecessary_whitespace(self):
        self.Data = re.sub(r'\s+', ' ', self.Data).strip()

    @staticmethod
    def removing_stop_word(txt):
        stop_words = set(stopwords.words('english'))
        x = txt.split()
        x = [word for word in x if word not in stop_words]
        return ' '.join(x)

    def removing_stop_words(self):
        self.Data = self.Data.apply(TextCleaner.removing_stop_word)

    def convert_to_lowercase(self):
        self.Data = self.Data.lower()

    @staticmethod
    def row_lemmatize(txt):
        x = txt.split()
        lemmatizer = nltk.stem.WordNetLemmatizer()
        x = [lemmatizer.lemmatize(word) for word in x]
        return ' '.join(x)

    def lemmatize(self):
        self.Data = self.Data.apply(TextCleaner.row_lemmatize)


    def clean(self):
        self.removing_punctuation_marks()
        self.removing_special_characters()
        self.removing_unnecessary_whitespace()
        self.convert_to_lowercase()
        self.removing_stop_words()
        self.lemmatize()
        return self.Data
        

