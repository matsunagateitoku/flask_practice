import spacy

# Load the English spaCy model
nlp = spacy.load("en_core_web_sm")

def process_text_with_spacy(text):
    """Process text with spaCy: tokenizes and performs POS tagging."""
    # Process the text using spaCy NLP pipeline
    doc = nlp(text)
    
    # Extract tokens and POS tags
    tokens_and_tags = [(token.text, token.pos_) for token in doc]
    
    return tokens_and_tags
