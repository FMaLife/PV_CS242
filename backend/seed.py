from app import create_app
from app.models import db
from app.models.user_model import User
from app.models.course_model import Course
from app.models.task_model import Task
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    print("Start insert seed data...")

    # ---- USER ----
    user = User.query.filter_by(email="test@mail.com").first()
    if not user:
        user = User(
            username="Hamtaro", 
            email="test@mail.com", 
            password="scrypt:32768:8:1$8EqCHzqFHFvkj6Jm$e2590466cc048002cce6b5952e863c99a16fff07065c6a2a65fc805027289ea5c783d825fa0fe75f91d727f5f02f256c00dc9f2783671d862caa5448fa3f8ec9")
        db.session.add(user)
        db.session.commit()

    # ---- COURSE ----
    course = Course.query.filter_by(_name="Math", user_id=user.id).first()
    if not course:
        course = Course(name="Python", course_code="CS242", course_weight=3, user_id=user.id)
        db.session.add(course)
        db.session.commit()

    # ---- TASK ----
    task = Task.query.filter_by(
        _title="Lab 1",
        course_id=course.id
    ).first()

    if not task:
        task = Task(
            title="Lab 1",
            description="Implement python programming using dict",
            deadline=datetime.utcnow() + timedelta(days=7),
            duration=2,
            emergency=True,
            score_weight=10,
            course_id=course.id
        )
        db.session.add(task)
        db.session.commit()

    print("Insert success !")