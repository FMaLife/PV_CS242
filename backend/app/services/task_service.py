from app.models import db
from app.models.task_model import Task
from app.models.course_model import Course
from datetime import datetime
from app.core.priority_engine import PriorityEngine

def create_task(title, deadline, score_weight, course_id,
                description=None, duration=None, emergency=False):
    
    # 🔥 convert ตรงนี้
    deadline = datetime.fromisoformat(deadline)

    task = Task(
        title=title,
        deadline=deadline,
        score_weight=score_weight,
        course_id=course_id,
        description=description,
        duration=duration,
        emergency=emergency
    )

    db.session.add(task)
    db.session.commit()

    return task


def get_all_tasks_by_user(user_id):
    return Task.query.join(Course).filter(Course.user_id == user_id).all()


def get_prioritized_tasks(user_id):
    tasks = get_all_tasks_by_user(user_id)
    engine = PriorityEngine(tasks)
    prioritized = engine.prioritize()

    result = []

    for item in prioritized:
        t = item["task"]
        result.append({
            "id": t.id,
            "title": t.get_title(),
            "description": t.description,
            "deadline": t.get_deadline().isoformat(),
            "duration": t.get_duration(),
            "emergency": t.is_emergency(),
            "score_weight": t.get_score_weight(),
            "status": t.get_status(),
            "course": {
                "id": t.course.id,
                "name": t.course.get_name(),
                "course_code": t.course.get_course_code()
            },
            "priority": {
                "score": round(item["score"], 2),
                "label": item["label"]
            }
        })

    return result


def get_task_by_id(task_id):
    return Task.query.get(task_id)


def update_task(task, **kwargs):
    if "title" in kwargs:
        task.set_title(kwargs["title"])

    if "deadline" in kwargs:
        task.set_deadline(kwargs["deadline"])

    if "duration" in kwargs:
        task.set_duration(kwargs["duration"])

    if "score_weight" in kwargs:
        task.set_score_weight(kwargs["score_weight"])

    db.session.commit()
    return task


def toggle_task_status(task_id, user_id):
    task = db.session.get(Task, task_id)

    if not task:
        return None

    # 🔒 check ownership
    if task.course.user_id != user_id:
        return None

    task.toggle_status()
    db.session.commit()

    return task

 