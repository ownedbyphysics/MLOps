from flask import Flask, request, jsonify, render_template
from model.model import predict_pipeline
from model.model import __version__ as model_version

app = Flask(__name__)



LANGUAGE_DICT = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "el": "Greek",
    "ar": "Arabic",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "tr": "Turkish",
    "da": "Danish",
    "sv": "Swedish",
    "ru": "Russian",
    "ta": "Tamil",
    "hi": "Hindi",
    "ml": "Malayalam",
    None: ' '
}

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    
    
    if request.method == "POST":
        text = request.form["text"]
        prediction = predict_pipeline(text)
        print(LANGUAGE_DICT[prediction])
        
    

    return render_template("index.html", model_version=model_version, 
                           prediction = LANGUAGE_DICT[prediction])
                      #     prediction=LANGUAGE_DICT(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
