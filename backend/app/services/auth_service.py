from app.models import db
from app.models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(username, email, password):
    existing = User.query.filter_by(email=email).first()
    if existing:
        return None, "Email already exists"

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return user, None


def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return None, "User not found"

    if not check_password_hash(user.get_password(), password):
        return None, "Invalid password"

    return user, None