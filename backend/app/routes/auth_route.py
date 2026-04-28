from flask import Blueprint, request, jsonify, session
from app.services.auth_service import login_user, register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    user, error = register_user(
        username=data.get("username"),
        email=data.get("email"),
        password=data.get("password")
    )

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "User created successfully",
        "user_id": user.id
    })


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user, error = login_user(
        email=data.get("email"),
        password=data.get("password")
    )

    if error:
        return jsonify({"error": error}), 401

    session["user_id"] = user.id
    session.permanent = True

    return jsonify({
        "message": "Login successful",
        "user_id": user.id
    })


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})