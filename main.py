from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


names = ["Bor", "Filip", "Meta", "Tanja"]


@app.route("/hello")
def hello():
    return render_template("hello.html", user=random.choice(names))


food = ["Pizza", "Burger", "Tortila", "Pasta"]


if __name__ == '__main__':
    app.run(use_reloader=True)
