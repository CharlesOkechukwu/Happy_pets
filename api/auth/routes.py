#!/usr/bin/python3
"""Create a Blueprint for routes in the auth package"""

# Imports
from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm
from . import auth
from .utils import hash_password
from api import db
from models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
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
        return "successful"
    return render_template('register.html', form=form)
