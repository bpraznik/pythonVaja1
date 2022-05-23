import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler!"
    current_year = datetime.datetime.now()
    return render_template("index.html", text=some_text, current=current_year)


@app.route("/about-me")
def about_me():
    about_list_1 = []
    return render_template("about.html", about_list=about_list_1)


if __name__ == '__main__':
    app.run(use_reloader=True)
