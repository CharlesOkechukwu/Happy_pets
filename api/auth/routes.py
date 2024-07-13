#!/usr/bin/python3
"""Create a Blueprint for routes in the auth package"""

# Imports
from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm, LoginForm
from . import auth # Import from __int__.py
from . import hash_password # Import from __int__.py
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
        return redirect (url_for('views.home'))
    return render_template('login.html', title='Sign In', form=form)