from flask import request, current_app
from twilio.request_validator import RequestValidator


def is_valid_twilio_request():
    auth_token = current_app.config.get("TWILIO_AUTH_TOKEN")

    if not auth_token:
        return False

    validator = RequestValidator(auth_token)

    signature = request.headers.get("X-Twilio-Signature")

    if not signature:
        return False

    return validator.validate(
        request.url,
        request.form,
        signature
    )