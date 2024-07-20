"""This module contains the Vet model class"""
from api import db
from flask_login import UserMixin


class Vet(db.Model, UserMixin):
    """Vet object model"""
    __tablename__ = 'vet'
    vet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(200), nullable=False)

    def get_id(self):
        """overried get_id method and return vet_id"""
        return self.vet_id