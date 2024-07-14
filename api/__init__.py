#!/usr/bin/python3
"""Flask App module"""

# Imports
import os
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


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

    # Initialize Flask-Login with the Flask app &
    # set the login view for Flask-Login to redirect to if a user needs to log in
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    
    from .views import views
    from .auth import auth


    # Register the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import the user model
    from models import User

    # Manage the user session
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Create the database if it does not exist
    with app.app_context():
        db.create_all()

    # Return the app to where it is called
    return app