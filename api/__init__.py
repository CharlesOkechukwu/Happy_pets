#!/usr/bin/python3
"""Flask App module"""

# Imports
import os
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy


# Add database and db name
db = SQLAlchemy()

def create_app(config_class='config.DevelopmentConfig'):
    """Initialize a flask app"""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    # Initialize cache and Ensure the cache is initialized with the app config
    cache = Cache(app)
    cache.init_app(app)

    # initialize the database with the app
    db.init_app(app)
    
    from .views import views
    from .auth import auth


    # Register the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import the user model
    from models import User

    # Create the database if it does not exist
    with app.app_context():
        db.create_all()

    # Return the app to where it is called
    return app