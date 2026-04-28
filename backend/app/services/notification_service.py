from datetime import datetime, timedelta
from app.models import Task, Course


def get_notifications(user_id):
    now = datetime.utcnow()
    next_24h = now + timedelta(hours=24)

    tasks = Task.query.join(Course).filter(
        Course.user_id == user_id
    ).all()

    due_soon_tasks = []

    for task in tasks:
        # ❌ ไม่เอางานที่เสร็จแล้ว
        if task.is_completed():
            continue

        deadline = task.get_deadline()

        # ✅ อยู่ในช่วง 24 ชม.
        if now <= deadline <= next_24h:
            due_soon_tasks.append(task)

    count = len(due_soon_tasks)

    # ✅ ไม่มีงานเลย
    if count == 0:
        return {
            "type": "INFO",
            "message": "No tasks due in the next 24 hours 🎉",
            "count": 0
        }

    # ✅ มีงาน
    return {
        "type": "DUE_SOON_24H",
        "message": f"You have {count} task(s) due in the next 24 hours",
        "count": count,
        "tasks": [
            {
                "id": t.id,
                "title": t.get_title(),
                "deadline": t.get_deadline().isoformat()
            }
            for t in due_soon_tasks
        ]
    }