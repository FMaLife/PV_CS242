from app.models import db
from app.models.course_model import Course


def create_course(name, course_code, course_weight, user_id):
    course = Course(name=name, course_code=course_code, course_weight=course_weight, user_id=user_id)

    db.session.add(course)
    db.session.commit()

    return course


def get_all_courses(user_id):
    return Course.query.filter_by(user_id=user_id).all()


def get_course_by_id(course_id):
    return Course.query.get(course_id)


def update_course(course_id, name=None, course_code=None, course_weight=None):
    course = Course.query.get(course_id)

    if not course:
        return None, "Course not found"

    if name is not None:
        course.set_name(name)

    if course_code is not None:
        course.set_course_code(course_code)

    if course_weight is not None:
        course.set_course_weight(course_weight)

    db.session.commit()
    return course, None