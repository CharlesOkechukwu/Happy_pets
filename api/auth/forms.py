#!/usr/bin/python3
"""Create a form module"""

from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User  # Assuming User model is in models/user.py and it import in the __init__.py to make available in the package

class RegistrationForm(FlaskForm):
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Enter your lastname"})
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter your firstname"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    phonenumber = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)], render_kw={"placeholder": "Enter your phone number"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm password"})

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('Email is already taken. Please choose a different one.', 'error')
            raise ValidationError('Email is already taken. Please choose a different one.')

    def validate_phonenumber(self, phonenumber):
        user = User.query.filter_by(phonenumber=phonenumber.data).first()
        if user:
            flash('Phone number is already taken. Please choose a different one.', 'error')
            raise ValidationError('Phone number is already taken. Please choose a different one.')