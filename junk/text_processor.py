# text_processor.py
import os
import sys
import spacy
from deep_translator import GoogleTranslator
from spacy import displacy
from io import StringIO

# Suppress warnings and output (to make it cleaner)
sys.stdout = open(os.devnull, 'w')

# Load the Chinese spaCy model
nlp = spacy.load("zh_core_web_sm")

# Function to process the Chinese text
def process_text(chinese_text):
    # Process text using spaCy
    doc = nlp(chinese_text)
    
    # Translate the Chinese text to English using GoogleTranslator
    translated_text = GoogleTranslator(source='auto', target='en').translate(chinese_text)
    
    # Extract Named Entities (NER)
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "start_char": ent.start_char,
            "end_char": ent.end_char
        })
    
    # Generate the NER visualization using displacy
    # We will use StringIO to capture the rendered HTML
    ner_html = StringIO()
    displacy.render(doc, style="ent", page=False, minify=True, jupyter=False, output=ner_html)
    ner_html_str = ner_html.getvalue()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    return {
        "original_text": chinese_text,
        "translated_text": translated_text,
        "entities": entities,
        "html_ner": ner_html_str  # Pass NER HTML as string
    }
