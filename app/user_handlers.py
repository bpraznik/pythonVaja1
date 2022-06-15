import datetime

from flask import Blueprint, render_template

from app.database import db
from app.models import User, Message

user_handlers = Blueprint('user_handlers', __name__)


@user_handlers.route("/users", methods=["GET"])
def users():
    ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
    latest_messages = db.query(Message).filter(Message.posted_at > ten_minutes_ago).all()
    latest_authors = set([message.author for message in latest_messages])
    active_users = db.query(User).filter(User.username.in_(latest_authors)).all()
    return render_template("users.html", users=active_users)


@user_handlers.route("/user/<user_id>", methods=["GET"])
def user_details(user_id):
    user = db.query(User).get(int(user_id))
    return render_template("user_details.html", user=user)
