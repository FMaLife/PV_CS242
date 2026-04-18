from app.models.user_model import User
from app.models import db

def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return None, "User not found"

    # FIX: use werkzeug from flask to hash password
    if user.password != password:
        return None, "Invalid password"

    return user, None