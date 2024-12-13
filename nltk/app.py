import nltk

from flask import Flask, render_template, request
nltk.download('punkt')  # For tokenization
nltk.download('averaged_perceptron_tagger')  # For POS tagging

# Initialize the Flask application
app = Flask(__name__)

# Route for both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def home():
    pos_tags = None  # Default to None if no POST request
    text = ''
    
    if request.method == 'POST':
        # Get the text from the form
        text = request.form['text']
        
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        
        # Perform POS tagging
        pos_tags = nltk.pos_tag(tokens)
    
    # Render the form and any results on the same page
    return render_template('index.html', pos_tags=pos_tags, text=text)

if __name__ == '__main__':
    app.run(debug=True)
