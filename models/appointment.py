"""appintment object model module"""
from api import db


class Appointment(db.Model):
    """implement the appointment object model"""
    a_id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    vet_id = db.Column(db.Integer, db.ForeignKey('vet.vet_id'), nullable=False)
    vet_name = db.Column(db.String(200), nullable=False)
    vet_specie = db.Column(db.String(200), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    appointment_type = db.Column(db.String(200), nullable=False)
    info = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(200), nullable=False)