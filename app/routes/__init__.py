from flask import Blueprint
from app.routes.webhook import webhook_bp


health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200