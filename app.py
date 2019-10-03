from flask import Flask, render_template, request
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texts = request.form["texts"]
        language = "English"
        return render_template("index.html", language=language)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
