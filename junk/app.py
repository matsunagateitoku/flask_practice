from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # This will hold the bolded word to display
    bold_word = None
    
    if request.method == "POST":
        # Get the input word from the form
        input_word = request.form.get("user_input")
        
        if input_word:
            bold_word = input_word  # Store the word to display in bold

    return render_template("index.html", bold_word=bold_word)

if __name__ == "__main__":
    app.run(debug=True)
