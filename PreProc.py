import re
import nltk
from nltk.corpus import stopwords


class PreProc:
    def __init__(self):
        # Download stopwords if not already present
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')

        self.stopword_set = set(stopwords.words('english'))

    def preprocessing(self, data_list):
        """
        Processes a list of strings (filenames or file content).
        """
        processed_list = []
        for text in data_list:
            # Convert to lowercase
            text = str(text).lower()

            # Remove punctuation and special characters
            text = re.sub(r'[^\w\s]', ' ', text)

            # Remove numbers
            text = re.sub(r'\d+', '', text)

            # Tokenize and remove stopwords
            words = text.split()
            filtered_words = [w for w in words if w not in self.stopword_set]

            processed_list.append(" ".join(filtered_words))

        return processed_list