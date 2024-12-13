from flask import Flask, render_template, request
from text_utils import convert_to_uppercase  # Import the function from text_utils.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bold_word = None
    
    if request.method == "POST":
        # Get the input word from the form
        input_word = request.form.get("user_input")
        
        if input_word:
            # Call the function from text_utils.py to convert the word to uppercase
            bold_word = convert_to_uppercase(input_word)

    return render_template("index.html", bold_word=bold_word)

if __name__ == "__main__":
    app.run(debug=True)
