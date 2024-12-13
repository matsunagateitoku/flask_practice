import nltk
from nltk import pos_tag, word_tokenize
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Ensure the necessary NLTK resources are downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

def process_phrase(phrase):
    """
    Process a phrase using NLTK.

    Args:
        phrase (str): The phrase to process.

    Returns:
        list: A list of tuples containing the word and its POS tag.
    """
    try:
        tokens = word_tokenize(phrase)
        tagged = pos_tag(tokens)
        return tagged
    except Exception as e:
        logging.error(f'Error processing phrase: {e}')
        raise