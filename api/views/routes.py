import os
from flask import render_template, request, flash, redirect, url_for, current_app, session
from api import db
from .forms import AddVaccinationForm, HealthRecordForm, GrowthRecordForm
from api.views import views
from models import Pet, Vet, Appointment
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

@views.route('/vet', methods=['GET'], strict_slashes=False)
@login_required
def vet():
    """vet doctor dashboard"""
    if session['vet_id'] is not None:
        vet_id = session['vet_id']
        vet = Vet.query.filter_by(vet_id=vet_id).first()
        appointments = Appointment.query.filter_by(vet_id=vet_id).order_by(Appointment.time.asc()).all()
        return render_template('vet_home.html', vet=vet, appointments=appointments)
    return redirect(url_for('auth.vet_login'))

@views.route('/vet/session/<pet_id>/<a_id>', strict_slashes=False)
@login_required
def vet_session(pet_id, a_id):
    """start pet vet session"""
    session['vet_session'] = pet_id
    vacc_form = AddVaccinationForm()
    health_form = HealthRecordForm()
    growth_form = GrowthRecordForm()
    pet = Pet.query.filter_by(id=pet_id).first()
    pet_age = pet.pet_age()
    vet_id = session['vet_id']
    vet = Vet.query.filter_by(vet_id=vet_id).first()
    appointment = Appointment.query.filter_by(a_id=a_id).first() 
    if pet is not None:
        return render_template('vet_session.html', pet=pet, vet=vet, appointment=appointment, pet_age=pet_age,
                               vacc_form=vacc_form, health_form=health_form, growth_form=growth_form)


@views.route('/vet/session/<a_id>/end', strict_slashes=False)
@login_required
def end_session(a_id):
    """end vet session"""
    session.pop('vet_session', None)
    #delete appointment from table
    appointment = Appointment.query.filter_by(a_id=a_id).first()
    db.session.delete(appointment)
    db.session.commit()
    return redirect(url_for('views.vet'))