"""Pet growth record object model"""
from api import db


class GrowthRecord(db.Model):
    """pet growth record object model"""
    __tablename__ = 'petgrowth'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    vet_id = db.Column(db.Integer, db.ForeignKey('vet.vet_id'), nullable=False)
    vet_name = db.Column(db.String(200), nullable=False)