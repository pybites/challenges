"""
application.py

Application factory and entry point
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set database
db = SQLAlchemy()


def create_app(development=True):
    app = Flask(__name__)

    # Load config:
    if development:
        app.config.from_object('settings.DevelopmentConfig')
    else:
        app.config.from_object('settings.ProductionConfig')

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import blueprints
    from pomodoro.views import pomodoro_app

    # Register blueprints
    app.register_blueprint(pomodoro_app)

    return app
