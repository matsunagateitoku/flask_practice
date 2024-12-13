from flask import Flask, render_template, request
import nltk
from nltk import pos_tag, word_tokenize

app = Flask(__name__)

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = request.form['phrase']
        tokens = word_tokenize(phrase)
        tagged = pos_tag(tokens)
        return render_template('index.html', phrase=phrase, tagged=tagged)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)