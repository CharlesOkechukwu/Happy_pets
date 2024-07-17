#!/usr/bin/python3
"""Create a Blueprint for routes in the auth package"""

# Imports
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from . import auth # Import from __int__.py
from . import hash_password, authenticate_user # Import from __int__.py
from api import db
from models import User
from api.views import views

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