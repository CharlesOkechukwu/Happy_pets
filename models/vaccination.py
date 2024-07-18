#!/usr/bin/python3
"""This module contains the Vaccination model."""
from api import db


class Vaccination(db.Model):
    """implement the vaccination object model"""
    __tablename__ = 'vaccination'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    vaccine_name = db.Column(db.String(200), nullable=False)
    dose_number = db.Column(db.Integer, nullable=False)
    date_administered = db.Column(db.Date, nullable=False)
    next_due_date = db.Column(db.Date, nullable=True)
    vet_name = db.Column(db.String(200), nullable=False)
    doses_left = db.Column(db.Integer, nullable=False)