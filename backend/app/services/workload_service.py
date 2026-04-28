from app.models.task_model import Task
from app.models.course_model import Course
from app.core.workload_analyzer import WorkloadAnalyzer


def get_workload_analysis(user_id, mode="weekly"):
    tasks = Task.query.join(Course).filter(Course.user_id == user_id).all()

    analyzer = WorkloadAnalyzer(tasks)

    if mode == "weekly":
        return analyzer.analyze_weekly()
    else:
        return analyzer.analyze_monthly()