"""module for update and add form classes"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateTimeField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User, Vet, Appointment, Pet, Vaccination, HealthRecord, GrowthRecord  # Assuming User model is in models/user.py and it import in the __init__.py to make available in the package


class AddVaccinationForm(FlaskForm):
    """Create AddVaccinationForm class form"""
    vaccine_name = StringField('Vaccine Name', validators=[DataRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Enter vaccine name"})
    dose_number = IntegerField('Dose Number', validators=[DataRequired()], render_kw={"placeholder": "Enter dose number"})
    next_due_date = DateField('Next Due Date', validators=[DataRequired()], render_kw={"placeholder": "Enter next vaccination due date"})
    doses_left = IntegerField('Dose Number Left', validators=[DataRequired()], render_kw={"placeholder": "Enter dose number left to complete vaccination"})
    submit = SubmitField('Add')


class HealthRecordForm(FlaskForm):
    """create add health record form"""
    vet_doctor = StringField('Vet Doctor', validators=[DataRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Enter vet doctor name"})
    symptoms = StringField('Symptoms', validators=[DataRequired(), Length(min=1, max=200)], render_kw={"placeholder": "Enter symptoms"})
    diagnosis = StringField('Diagnosis', validators=[DataRequired(), Length(min=1, max=200)], render_kw={"placeholder": "Enter diagnosis"})
    treatment = StringField('Treatment', validators=[DataRequired(), Length(min=1, max=200)], render_kw={"placeholder": "Enter treatment"})
    status = StringField('Final Comments', validators=[DataRequired(), Length(min=1, max=200)], render_kw={"placeholder": "Enter final comments"})
    submit = SubmitField('Add')


class GrowthRecordForm(FlaskForm):
    """add pet growth recorf form"""
    month = StringField('Month', validators=[DataRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Enter month"})
    year = IntegerField('Year', validators=[DataRequired()], render_kw={"placeholder": "Enter year"})
    weight = IntegerField('Weight', validators=[DataRequired()], render_kw={"placeholder": "Enter weight"})
    height = IntegerField('Height', validators=[DataRequired()], render_kw={"placeholder": "Enter height"})
    submit = SubmitField('Add')