from flask import Flask, render_template, request
from text_utils import process_text_with_spacy  # Import the function from text_utils.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    processed_text = None
    
    if request.method == "POST":
        # Get the input text from the form
        input_text = request.form.get("user_input")
        
        if input_text:
            # Call the function from text_utils.py to process the text using spaCy
            processed_text = process_text_with_spacy(input_text)

    return render_template("index.html", processed_text=processed_text)

if __name__ == "__main__":
    app.run(debug=True)
