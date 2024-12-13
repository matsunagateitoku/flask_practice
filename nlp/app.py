from flask import Flask, render_template, request, flash
from nlp import process_phrase

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = request.form.get('phrase')
        if not phrase:
            flash('Please enter a phrase')
            return render_template('index.html')
        try:
            tagged = process_phrase(phrase)
            return render_template('index.html', phrase=phrase, tagged=tagged)
        except Exception as e:
            flash('Error processing phrase. Please try again.')
            return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)