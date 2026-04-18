from app.models.user_model import User
from app.models import db

def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return None, "User not found"

    if user.password != password:   # ❗ เดี๋ยวค่อย hash ทีหลัง
        return None, "Invalid password"

    return user, None