from flask import Blueprint, jsonify, session
from app.services.notification_service import get_notifications

notification_bp = Blueprint("notification", __name__)


@notification_bp.route("", methods=["GET"])
def get_all():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    notifications = get_notifications(user_id)

    return jsonify(notifications)