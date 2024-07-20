#!/usr/bin/python3
"""Flask App config module"""

DB_NAME = 'HappyPet_db'

class Config:
    SECRET_KEY = 'holiz_15'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'  # Flask-Caching related config

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}_dev.db'.format(DB_NAME)

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}_test.db'.format(DB_NAME)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}.db'.format(DB_NAME)

class CharlesConfig(Config):
    username = 'root'
    password = ''
    host = 'localhost'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, DB_NAME)
