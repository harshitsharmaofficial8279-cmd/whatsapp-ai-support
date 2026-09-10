from flask import Blueprint, request, jsonify
from app.security.webhook_security import is_valid_twilio_request

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():

    if not is_valid_twilio_request():
        return jsonify({
            "status": "error",
            "message": "Invalid webhook signature"
        }), 403

    data = request.form.to_dict()

    return jsonify({
        "status": "received",
        "message": "WhatsApp webhook received"
    }), 200