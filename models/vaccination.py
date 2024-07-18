"""This module contains the Vaccination model."""
from api import db
from sqlalchemy.sql import func


class Vaccination(db.Model):
    """implement the vaccination object model"""
    __tablename__ = 'vaccination'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    vaccine_name = db.Column(db.String(200), nullable=False)
    dose_number = db.Column(db.Integer, nullable=False)
    date_administered = db.Column(db.DateTime(timezone=True), server_default=func.now())
    next_due_date = db.Column(db.Date, nullable=True)
    vet_id = db.Column(db.Integer, db.ForeignKey('vet.vet_id'), nullable=False)
    vet_name = db.Column(db.String(200), nullable=False)
    doses_left = db.Column(db.Integer, nullable=False)