from app.database import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)
    posted_at = db.Column(db.DateTime)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    session_token = db.Column(db.String)
