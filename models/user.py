#!/usr/bin/python3
"""Database model for user account"""

# Import modules/variables
from api import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Begin defining class
class User(db.Model, UserMixin):
    """User's Table"""
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phonenumber = db.Column(db.String(20))
    password = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())