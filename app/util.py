from app.database import db
from app.models import User


def get_user_from_request(request):
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()
    return user
