from app.models import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column("username", db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)

    courses = db.relationship('Course', backref='user', lazy=True)

    # ✅ constructor
    def __init__(self, username, email, password):
        self.set_username(username)
        self.email = email
        self.set_password(password)

    # ✅ getter / setter
    def get_username(self):
        return self._username

    def set_username(self, username):
        if not username or len(username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, hashed_password):
        if not hashed_password:
            raise ValueError("Password cannot be empty")
        self._password = hashed_password

    # ✅ behavior
    def check_password(self, password, verify_func):
        return verify_func(password, self._password)

    def get_course_count(self):
        return len(self.courses)

    # ✅ business logic (non-trivial)
    def can_create_course(self, max_courses=10):
        return len(self.courses) < max_courses