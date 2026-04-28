from flask import Blueprint, request, jsonify, session
from app.services.course_service import (
    create_course,
    get_all_courses,
    get_course_by_id,
    update_course
)

course_bp = Blueprint("course", __name__)


@course_bp.route("", methods=["POST"])
def create():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()

    course = create_course(
        user_id=user_id,
        name=data.get("name"),
        course_code=data.get("course_code"),
        course_weight=data.get("course_weight")
    )

    return jsonify({"message": "Course created", "id": course.id})


@course_bp.route("", methods=["GET"])
def get_all():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    courses = get_all_courses(user_id)

    return jsonify([
        {"id": c.id, "name": c._name, "course_code": c._course_code, "course_weight": c._course_weight}
        for c in courses
    ])


@course_bp.route("/<int:course_id>", methods=["GET"])
def get_one(course_id):
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    course = get_course_by_id(course_id)

    return jsonify({
        "id": course.id,
        "name": course._name,
        "course_code": course._course_code,
        "course_weight": course._course_weight
    })


@course_bp.route("/<int:course_id>", methods=["PUT"])
def update(course_id):
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    course, error = update_course(
        course_id,
        name=data.get("name"),
        course_code=data.get("course_code"),
        course_weight=data.get("course_weight")
    )

    if error:
        return jsonify({"error": error}), 404

    return jsonify({"message": "Course updated"})