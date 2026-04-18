from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.user_model import User
from app.models.course_model import Course
from app.models.task_model import Task