# one.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)

def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
