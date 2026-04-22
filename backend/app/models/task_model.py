from app.models import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)  # ชั่วโมง/นาที (แล้วแต่คุณ define)
    emergency = db.Column(db.Boolean, default=False)
    score_weight = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default="pending")

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)