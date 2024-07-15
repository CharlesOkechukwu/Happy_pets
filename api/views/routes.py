import os
from flask import render_template, request, flash, redirect, url_for, current_app
from api import db
from api.views import views
from models import Pet
from datetime import date
from flask_login import login_required
from . import upload_photo


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pet/add', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def add_pet():
    if request.method == 'POST':
        name = request.form.get('name')
        specie = request.form.get('specie')
        breed = request.form.get('breed')
        birth_date = request.form.get('birth_date')
        color = request.form.get('color')
        photo = request.files.get('photo')
        
        pet = Pet()
        pet.owner_id = 1
        if name == '':
            flash("You must enter your pet name!!", 'error')
        else:
            pet.name = name
        if specie == '':
            flash("Enter your pet type eg Dog, Cat etc", 'error')
        else:
            pet.specie = specie
        if breed == '':
            flash("Enter your pet's breed", "error")
        else:
            pet.breed = breed
        if birth_date == '':
            flash("Enter pet's date of date of birth", 'error')
        else:
            pet.birth_date = date(*map(int, birth_date.split('-')))
        if color == '':
            flash("Enter pet's color", 'error')
        else:
            pet.color = color
        photo_path = upload_photo(photo)
        if photo_path is not None:
            pet.photo = photo_path
            db.session.add(pet)
            db.session.commit()
            flash("Pet added successfully", 'success')
        return redirect(url_for('views.add_pet'))
    return render_template("add_pet.html")


@views.route('/health', methods=['GET'], strict_slashes=False)
def health():
    return render_template("health_tracker.html")

@views.route('/base')
def index():
    return render_template('base.html')