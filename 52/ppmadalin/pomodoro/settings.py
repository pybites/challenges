"""
settings.py

Contains all the settings of the app
"""
import os
import pathlib


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = pathlib.Path(__file__).parent.joinpath('instance/pomodoro.db')
    DB_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass
