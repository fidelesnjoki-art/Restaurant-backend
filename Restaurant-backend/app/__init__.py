from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    allowed = [
        "http://localhost:5173",
        os.environ.get("FRONTEND_URL", ""),
    ]
    CORS(app, origins=[o for o in allowed if o])
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp
    app.register_blueprint(bp, url_prefix="/api")

    return app
