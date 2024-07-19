#!/usr/bin/python3
"""Create a Blueprint for routes in the auth package"""

# Imports
from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm, VetRegistrationForm, VetLoginForm, AppointmentForm
from . import auth # Import from __int__.py
from . import hash_password, authenticate_user, authenticate_vet# Import from __int__.py
from api import db
from models import User, Vet, Appointment
from api.views import views, upload_photo
from datetime import datetime


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Handle POST api/auth/register"""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process form data (e.g., create user, save to database)
        hashed_password = hash_password(form.password.data)
        new_user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            phonenumber=form.phonenumber.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Handle POST api/auth/login"""
    if current_user.is_authenticated:
        return redirect(url_for('views.userdashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate_user(form.email.data)
        if user:
            login_user(user)
            return redirect (url_for('views.userdashboard'))
    return render_template('login.html', title='Sign In', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))


# Routes for vet dashboard
@auth.route('/vet/register', methods=['GET', 'POST'], strict_slashes=False)
def register_vet():
    """handles vet registration"""
    form = VetRegistrationForm()
    if form.validate_on_submit():  
        hashed_password = hash_password(form.password.data)
        new_vet = Vet(
            name=form.name.data,
            email=form.email.data,
            phonenumber=form.phonenumber.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            country=form.country.data,
            password=hashed_password
        )
        photo_path = upload_photo(form.photo.data)
        if photo_path is not None:
            new_vet.photo = photo_path
            db.session.add(new_vet)
            db.session.commit()
            flash('Vet account created successfully', 'success')
            return redirect(url_for('auth.register_vet'))
    else:
        print(form.errors)
    return render_template('register_vet.html', title='Register Vet', form=form)


@auth.route('/vet/login', methods=['GET', 'POST'], strict_slashes=False)
def vet_login():
    """Handle vet Doctor Login"""
    form = VetLoginForm()
    if form.validate_on_submit():
        vet = authenticate_vet(form.email.data)
        if vet:
            login_user(vet)
            session['vet_id'] = vet.vet_id
            return redirect(url_for('views.vet'))
    return render_template('vet_login.html', title='Vet Sign In', form=form)


@auth.route('/create_appointment', methods=['GET', 'POST'])
@login_required
def create_appointment():
    user_id = current_user.get_id()  # get the id of the user
    form = AppointmentForm(user_id=user_id)
    if form.validate_on_submit():
        appointment = Appointment(
            pet_id=form.pet_id.data,
            vet_id=form.vet_id.data,
            time=form.time.data,
            appointment_type=form.appointment_type.data,
            contact=form.contact.data
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('views.home'))
    else:
        print(form.errors)
        print(form.data)
    return render_template('create_appointment.html', form=form)