from flask import Flask, render_template, request
from iso639 import languages
from langdetect import detect
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")


def get_language(texts):
    try:
        alpha2 = detect(texts).split("-")[0]
    except:
        return "something I don't comprehend"
    else:
        return languages.get(alpha2=alpha2).name


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texts = request.form["texts"]
        language = get_language(texts)
        return render_template("index.html", language=language)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
