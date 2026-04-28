from app.models import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column("name", db.String(255), nullable=False)
    _course_code = db.Column("course_code", db.String(10), nullable=False)
    _course_weight = db.Column("course_weight", db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    tasks = db.relationship('Task', backref='course', lazy=True)

    # ✅ constructor
    def __init__(self, name, course_code, course_weight, user_id):
        self.set_name(name)
        self.set_course_code(course_code)
        self.set_course_weight(course_weight)
        self.user_id = user_id

    # ✅ getter / setter
    def get_name(self):
        return self._name

    def set_name(self, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Course name cannot be empty")
        self._name = name

    def get_course_code(self):
        return self._course_code

    def set_course_code(self, course_code):
        if not course_code:
            raise ValueError("Course code cannot be empty")
        self._course_code = course_code

    def get_course_weight(self):
        return self._course_weight

    def set_course_weight(self, weight):
        if weight <= 0:
            raise ValueError("Course weight must be positive")
        self._course_weight = weight

    # ✅ behavior
    def get_task_count(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.get_status() == "done"]

    # ✅ business logic (non-trivial)
    def calculate_progress(self):
        total = len(self.tasks)
        if total == 0:
            return 0.0
        completed = len(self.get_completed_tasks())
        return completed / total

    def get_weight_ratio(self, max_weight=3):
        return self._course_weight / max_weight