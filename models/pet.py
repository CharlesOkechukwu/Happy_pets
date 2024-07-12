#!/usr/bin/python3
"""module for pet object model"""
from api import db


class Pet(db.Model):
    """pet object model"""
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    color = db.Column(db.String(200), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)