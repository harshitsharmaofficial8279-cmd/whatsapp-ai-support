from flask import Flask
from app.config import Config
from app.database import db
from app.database import models
from app.routes import health_bp
from app.routes.webhook import webhook_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///whatsapp_support.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(webhook_bp)

    return app
