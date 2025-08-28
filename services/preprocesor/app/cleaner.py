import re
import nltk
from nltk.corpus import stopwords
import string
nltk.download('stopwords')

class TextCleaner:
    def __init__(self):
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def _remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def _remove_special_characters(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def _remove_unnecessary_whitespace(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def _to_lowercase(self, text):
        return text.lower()

    def _remove_stopwords(self, text):
        words = text.split()
        return ' '.join([word for word in words if word not in self.stop_words])

    def _lemmatize(self, text):
        words = text.split()
        return ' '.join([self.lemmatizer.lemmatize(word) for word in words])

    def clean(self, text: str):
        if not isinstance(text, str):
            return ""

        text = self._remove_punctuation(text)
        text = self._remove_special_characters(text)
        text = self._remove_unnecessary_whitespace(text)
        text = self._to_lowercase(text)
        text = self._remove_stopwords(text)
        text = self._lemmatize(text)
        return text