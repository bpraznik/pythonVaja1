from flask import Flask, render_template, request

from app.database import db
from app.message_handlers import message_handlers
from app.models import Message
from app.profile_handlers import profile_handlers
from app.user_handlers import user_handlers
from app.util import get_user_from_request

app = Flask(__name__)
app.register_blueprint(profile_handlers)
app.register_blueprint(user_handlers)
app.register_blueprint(message_handlers)

db.create_all()


@app.route("/", methods=["GET"])
def index():
    user = get_user_from_request(request)
    messages = db.query(Message).all()

    return render_template("index.html", messages=messages, user=user)


if __name__ == '__main__':
    app.run()
