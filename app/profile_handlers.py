import hashlib
import uuid

from flask import Blueprint, request, render_template, url_for, redirect, make_response

from app.database import db
from app.models import User
from app.util import get_user_from_request

profile_handlers = Blueprint('profile_handlers', __name__)


@profile_handlers.route("/login", methods=["POST"])
def login():
    username = request.form.get("user-username")
    password = request.form.get("user-password")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user = db.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username, password=hashed_password)
        user.save()

    if user.password != hashed_password:
        print("Invalid password attempt")
        return redirect(url_for('index'))

    session_token = str(uuid.uuid4())

    user.session_token = session_token
    user.save()

    response = make_response(redirect(url_for('index')))
    response.set_cookie("session_token", session_token, httponly=True, samesite="Strict", max_age=60*60*24*2)
    return response


@profile_handlers.route("/logout", methods=["GET"])
def logout():
    user = get_user_from_request(request)
    user.session_token = None
    response = make_response(redirect(url_for('index')))
    response.delete_cookie("session_token")
    return response


@profile_handlers.route("/profile", methods=["GET"])
def profile():
    user = get_user_from_request(request)
    return render_template("profile.html", user=user)


@profile_handlers.route("/profile/edit", methods=["GET", "POST"])
def profile_edit():
    user = get_user_from_request(request)

    if request.method == "GET":
        if user:
            return render_template("profile_edit.html", user=user)
    elif request.method == "POST":
        name = request.form.get("profile-name")
        email = request.form.get("profile-email")

        user.username = name
        user.email = email

        user.save()

    return redirect(url_for("index"))


@profile_handlers.route("/profile/delete", methods=["GET", "POST"])
def profile_delete():
    user = get_user_from_request(request)

    if request.method == "GET":
        if user:
            return render_template("profile_delete.html", user=user)
    elif request.method == "POST":
        user.delete()

    return redirect(url_for("index"))
