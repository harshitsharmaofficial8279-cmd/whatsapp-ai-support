from flask import Blueprint, request, jsonify

from app.security.webhook_security import is_valid_twilio_request
from app.services.conversation_service import (
    get_or_create_conversation,
    save_message
)
from app.services.ai_service import generate_ai_response
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

        ai_response = generate_ai_response(message_text)

        save_message(
            conversation_id=conversation.id,
            sender="ai",
            message_text=ai_response
        )

        return jsonify({
            "status": "success",
            "message": "Message processed successfully",
            "ai_response": ai_response
        }), 200

    except Exception:
        db.session.rollback()

        return jsonify({
            "status": "error",
            "message": "Unable to process message"
        }), 500
