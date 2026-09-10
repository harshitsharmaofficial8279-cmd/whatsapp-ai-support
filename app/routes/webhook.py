from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    data = request.form.to_dict()

    return jsonify({
        "status": "received",
        "message": "WhatsApp webhook received"
    })