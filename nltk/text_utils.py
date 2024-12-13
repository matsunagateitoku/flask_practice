import nltk
from typing import List, Tuple

# Download necessary datasets for tokenization and POS tagging
try:
    nltk.download('punkt_tab')  # For tokenization
    nltk.download('averaged_perceptron_tagger')  # For POS tagging
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")

def process_text_with_nltk(text: str) -> List[Tuple[str, str]]:
    """
    Process text with NLTK: tokenizes and performs POS tagging.

    Args:
        text (str): The input text to process.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the word and its POS tag.

    Raises:
        Exception: If an error occurs during text processing.
    """
    try:
        # Tokenize the text into words
        words = nltk.word_tokenize(text)
        
        # Perform part-of-speech (POS) tagging
        tagged_words = nltk.pos_tag(words)
        
        return tagged_words
    except Exception as e:
        print(f"Error processing text: {e}")
        raise



		 import nltk

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "NLTK is a powerful library for natural language processing."

# Tokenize the text (split it into words)
tokens = nltk.word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

# Display the POS tags
print(pos_tags)
