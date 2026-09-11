from flask import Blueprint, request, jsonify

from app.security.webhook_security import is_valid_twilio_request
from app.services.conversation_service import (
    get_or_create_conversation,
    save_message
)
from app.database import db


webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():

    if not is_valid_twilio_request():
        return jsonify({
            "status": "error",
            "message": "Invalid webhook signature"
        }), 403

    phone_number = request.form.get("From")
    message_text = request.form.get("Body")

    if not phone_number or not message_text:
        return jsonify({
            "status": "error",
            "message": "Missing sender or message"
        }), 400

    try:
        conversation = get_or_create_conversation(phone_number)

        save_message(
            conversation_id=conversation.id,
            sender="user",
            message_text=message_text
        )

        return jsonify({
            "status": "received",
            "message": "Message saved successfully"
        }), 200

    except Exception:
        db.session.rollback()

        return jsonify({
            "status": "error",
            "message": "Unable to process message"
        }), 500
