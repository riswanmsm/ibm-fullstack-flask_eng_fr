from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    # The function should take the English text as input through the request parameter and return a string
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    # The function should take the French text as input through the request parameter and return a string
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
