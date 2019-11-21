import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from iso639 import languages
from langdetect import detect
from whitenoise import WhiteNoise

from forms import TextInputForm


app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


def get_language(texts):
    if not texts:
        return None

    try:
        alpha2 = detect(texts).split("-")[0]
    except:
        return "something I don't comprehend"
    else:
        return languages.get(alpha2=alpha2).name


@app.route("/", methods=["get", "post"])
def index():
    form = TextInputForm(request.form)
    language = get_language(form.text_input.data)

    return render_template("index.html", form=form, language=language)


if __name__ == "__main__":
    app.run(debug=True)
