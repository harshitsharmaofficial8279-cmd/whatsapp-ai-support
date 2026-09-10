from flask import Flask


def create_app():
    app = Flask(__name__)

    return app
import os

from dotenv import load_dotenv
from flask import Flask


load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv("APP_NAME", "WhatsApp AI Support")

    return app
import os

from dotenv import load_dotenv
from flask import Flask

from app.routes import health_bp


load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv(
        "APP_NAME",
        "WhatsApp AI Support"
    )

    app.register_blueprint(health_bp)

    return app