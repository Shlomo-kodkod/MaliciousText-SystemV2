import re
import nltk
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
nltk.download('wordnet')


logger = logging.getLogger(__name__)


class TextCleaner:
    def __init__(self):
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def _remove_punctuation(self, text: str) -> str:
        """
        Remove all punctuation marks from the text.
        """
        return re.sub(r'\s+', ' ', text).strip()

    def _to_lowercase(self, text: str) -> str:
        """
        Convert text to lowercase.
        """
        return text.lower()

    def _remove_stopwords(self, text: str) -> str:
        """
        Remove common English stopwords from the text.
        """
        words = text.split()
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def _lemmatize(self, text: str) -> str:
        """
        Lemmatize words in the text to their base form.
        """
        words = text.split()
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(lemmatized_words)

    def clean(self, text: str) -> str:
        text = self._remove_punctuation(text)
        text = self._remove_special_characters(text)
        text = self._remove_unnecessary_whitespace(text)
        text = self._to_lowercase(text)
        text = self._remove_stopwords(text)
        text = self._lemmatize(text)
        return text


