from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = None
    if request.method == "POST":
        chinese_text = request.form.get("user_input")
        if chinese_text:
            # Translate the Chinese text to English
            translated_text = GoogleTranslator(source='zh', target='en').translate(chinese_text)
    
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
