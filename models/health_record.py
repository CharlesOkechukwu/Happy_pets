"""create health record model"""
from datetime import datetime
from sqlalchemy.sql import func
from api import db

class HealthRecord(db.Model):
    """health record object model"""
    __tablename__ = 'health_record'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    vet_id = db.Column(db.Integer, db.ForeignKey('vet.vet_id'), nullable=False)
    vet_doctor = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    symptoms = db.Column(db.String(255), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    treatment = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(100), nullable=False)
