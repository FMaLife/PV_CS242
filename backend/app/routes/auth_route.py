from flask import Blueprint, request, jsonify, session
from app.services.auth_service import login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user, error = login_user(
        email=data.get('email'),
        password=data.get('password')
    )

    if error:
        return jsonify({"error": error}), 401

    # set session
    session['user_id'] = user.id

    return jsonify({
        "message": "login success",
        "user_id": user.id
    })