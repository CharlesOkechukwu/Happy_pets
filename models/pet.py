#!/usr/bin/python3
"""module for pet object model"""
from api import db
from datetime import date


class Pet(db.Model):
    """pet object model"""
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    specie = db.Column(db.String(200), nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    color = db.Column(db.String(200), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    photo = db.Column(db.String(200), nullable=False)

    def pet_age(self):
        """calculate pet age"""
        today = date.today()
        date_of_birth = self.birth_date
        dob_split = str(date_of_birth).split('-')
        dob_year = int(dob_split[0])
        dob_month = int(dob_split[1])
        dob_day = int(dob_split[2])
        age = today.year - dob_year - ((today.month, today.day) < (dob_month, dob_day))
        return age