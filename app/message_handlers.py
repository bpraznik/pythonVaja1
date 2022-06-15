import datetime

from flask import Blueprint, request, redirect

from app.models import Message
from app.util import get_user_from_request

message_handlers = Blueprint('message_handlers', __name__)


@message_handlers.route("/add-message", methods=["POST"])
def add_message():
    user = get_user_from_request(request)
    message = request.form.get("text")
    now = datetime.datetime.now()

    message = Message(author=user.username, text=message, posted_at=now)
    message.save()
    return redirect("/")
