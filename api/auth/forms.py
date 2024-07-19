#!/usr/bin/python3
"""Form module"""

# Imports
from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField, DateTimeField
from . import verify_password # Import from __int__.py
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User  # Assuming User model is in models/user.py and it import in the __init__.py to make available in the package
from models import Vet, Appointment, Pet
from wtforms.fields import DateTimeLocalField


# form for registration
class RegistrationForm(FlaskForm):
    """Create RegistrationForm class form"""
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Enter your lastname"})
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter your firstname"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    phonenumber = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)], render_kw={"placeholder": "Enter your phone number"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('Email is already taken. Please choose a different one.', 'error')
            raise ValidationError('Email is already taken. Please choose a different one.')

    def validate_phonenumber(self, phonenumber):
        """Verify the phone number field from the form is already taken"""
        user = User.query.filter_by(phonenumber=phonenumber.data).first()
        if user:
            flash('Phone number is already taken. Please choose a different one.', 'error')
            raise ValidationError('Phone number is already taken. Please choose a different one.')
        
    def validate_phonenumber(self, phonenumber):
        """Verify if the phonenmber from the form is integer"""
        if not phonenumber.data.isdigit():
            flash('Phone number must be digit only.', 'error')
            raise ValidationError('Phone number must be digit only.')
        
    def validate_confirm_password(self, confirm_password):
        """Check password equality"""
        if confirm_password.data != self.password.data:
            flash('Passwords must match, type again.', 'error')
            raise ValidationError('Passwords must match, type again.')


# Form for login       
class LoginForm(FlaskForm):
    """Create LoginForm class form"""
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    submit = SubmitField('Sign in')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = User.query.filter_by(email=email.data).first()
        if not user:
            flash('Email is does not exist, check the email and try again.', 'error')
            raise ValidationError('Email is does not exist, check the email and try again')

    def validate_password(self, password):
        """Verify the password field from the form"""
        user = User.query.filter_by(email=self.email.data).first()
        if user and not verify_password(user.password, password.data):
            flash('Incorrect password, try again.', 'error')
            raise ValidationError('Incorrect password, try again.')

        
# Vet Form
class VetRegistrationForm(FlaskForm):
    """Create VetRegistrationForm class form"""
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=30)],render_kw={"placeholder": "Enter your name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    phonenumber = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)], render_kw={"placeholder": "Enter your phone number"})
    address = StringField('Address', validators=[DataRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Enter your address"})
    city = StringField('City', validators=[DataRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Enter your city"})
    state = StringField('State', validators=[DataRequired(), Length(min=3, max=30)], render_kw={"placeholder": "Enter your state"})
    country = StringField('Country', validators=[DataRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Enter your country"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm password"})
    photo = FileField('Photo', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = Vet.query.filter_by(email=email.data).first()
        if user:
            flash('Email is already taken. Please choose a different one.', 'error')
            raise ValidationError('Email is already taken. Please choose a different one.')

    def validate_phonenumber(self, phonenumber):
        """Verify the phone number field from the form is already taken"""
        user = Vet.query.filter_by(phonenumber=phonenumber.data).first()
        if user:
            flash('Phone number is already taken. Please choose a different one.', 'error')
            raise ValidationError('Phone number is already taken. Please choose a different one.')
    
    def validate_phonenumber(self, phonenumber):
        """Verify if the phonenmber from the form is integer"""
        if not phonenumber.data.isdigit():
            flash('Phone number must be digit only.', 'error')
            raise ValidationError('Phone number must be digit only.')
    
    def validate_country(self, country):
        """Verify the country field from the form"""
        allowed_countries = ['Nigeria', 'Ghana', 'Kenya', 'South Africa']
        if country.data not in allowed_countries:
            flash('Country not allowed. Please choose a different one.', 'error')
            raise ValidationError('Country not allowed! Only Nigeria, South Africa, Ghana and Kenya are allowed.')
        
    def validate_confirm_password(self, confirm_password):
        """Check password equality"""
        if confirm_password.data != self.password.data:
            flash('Passwords must match, type again.', 'error')
            raise ValidationError('Passwords must match, type again.')


class VetLoginForm(FlaskForm):
    """Create VetLoginForm class form"""
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    submit = SubmitField('Sign in')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = Vet.query.filter_by(email=email.data).first()
        if not user:
            flash('Email is does not exist, check the email and try again.', 'error')
            raise ValidationError('Email is does not exist, check the email and try again')

    def validate_password(self, password):
        """Verify the password field from the form"""
        user = Vet.query.filter_by(email=self.email.data).first()
        if user and not verify_password(user.password, password.data):
            flash('Incorrect password, try again.', 'error')
            raise ValidationError('Incorrect password, try again.')


# Booking appointment
class AppointmentForm(FlaskForm):
    pet_id = SelectField('Pet', coerce=int, validators=[DataRequired()])
    vet_id = SelectField('Vet', coerce=int, validators=[DataRequired()])
    time = DateTimeLocalField('Appointment Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    appointment_type = StringField('Appointment Type', validators=[DataRequired()], render_kw={"placeholder": "Reason"})
    contact = StringField('Contact Information', validators=[DataRequired()])
    submit = SubmitField('Book Appointment')


    def __init__(self, user_id, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.pet_id.choices = [(pet.id, pet.name) for pet in Pet.query.filter_by(owner_id=user_id).all()]
        self.vet_id.choices = [(vet.vet_id, vet.name) for vet in Vet.query.all()]