#!/usr/bin/python3
"""Routes fro Views module"""

import os
from flask import render_template, request, flash, redirect, url_for, current_app, session
from api import db
from .forms import AddVaccinationForm, HealthRecordForm, GrowthRecordForm
from api.views import views
from models import Pet, Vet, Appointment
from .forms import AddVaccinationForm, HealthRecordForm, GrowthRecordForm
from models import Pet, Vet, Appointment, Vaccination, HealthRecord, GrowthRecord
from datetime import date, datetime
from flask_wtf import csrf
from flask_login import login_required, current_user
from . import upload_photo


@views.route('/')
def home():
    """GET api/views/home"""
    return render_template("home.html", title='Home page')


@views.route('/pet/add', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def add_pet():
    """GET api/views/pet/add"""
    if request.method == 'POST':
        name = request.form.get('name')
        specie = request.form.get('specie')
        breed = request.form.get('breed')
        birth_date = request.form.get('birth_date')
        color = request.form.get('color')
        photo = request.files.get('photo')
        
        pet = Pet()
        pet.owner_id = current_user.id # Use current_user.id to set the owner_id
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
            return redirect(url_for('views.userdashboard'))
    return render_template("add_pet.html")


@views.route('/health/<pet_id>', methods=['GET'], strict_slashes=False)
@login_required
def health(pet_id):
    """GET api/views/health/<pet_id>"""
    pet = Pet.query.filter_by(id=pet_id).first()
    vaccinations = Vaccination.query.filter_by(pet_id=pet_id).order_by(Vaccination.date_administered.desc()).all()
    health_records = HealthRecord.query.filter_by(pet_id=pet_id).order_by(HealthRecord.date.desc()).all()
    growth_records = GrowthRecord.query.filter_by(pet_id=pet_id).order_by(GrowthRecord.month.desc()).all()
    appointments = Appointment.query.filter_by(pet_id=pet_id).order_by(Appointment.time.desc()).all()
    return render_template("health_tracker.html", user=current_user, pet=pet,
                           vaccinations=vaccinations, health_records=health_records,
                           growth_records=growth_records, appointments=appointments)


@views.route('/userdashboard')
@login_required
def userdashboard():
    """Rendder user dashboard"""
    # Retrieve the logged-in user's pets
    user_pets = Pet.query.filter_by(owner_id=current_user.id).all()
    return render_template('userdashboard.html', user=current_user, pets=user_pets)


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

@views.route('/vet/session/add/vaccination/<a_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def add_vaccine(a_id):
    """add pet vaccination record"""
    form = AddVaccinationForm()
    a_id = a_id
    appointment = Appointment.query.filter_by(a_id=a_id).first()
    if session.get('vet_session', None) is not None:
        pet_id = session['vet_session']
        vet_id = session['vet_id']
    else:
        flash('Warning: No vet session started! Start a vet session to add vaccination record', 'error')
    if request.method == 'POST' and session.get('vet_session', None) is not None:
        if form.validate_on_submit():
            vaccine_name = form.vaccine_name.data
            dose_number = form.dose_number.data
            next_due_date = form.next_due_date.data
            doses_left = form.doses_left.data
            vet = Vet.query.filter_by(vet_id=vet_id).first()
            vet_name = vet.name
            date_administered = datetime.now()
            vaccination = Vaccination(pet_id=pet_id, vaccine_name=vaccine_name,
                                        dose_number=dose_number, date_administered=date_administered,
                                        next_due_date=next_due_date, vet_id=vet_id, vet_name=vet_name,
                                        doses_left=doses_left)
            db.session.add(vaccination)
            db.session.commit()
            flash("Vaccination record added successfully", 'success')
            return redirect(url_for('views.vet_session', pet_id=pet_id, a_id=a_id))
        flash('Error adding vaccination record', 'error')
    return render_template('add_vaccination.html', vacc_form=form, appointment=appointment)


@views.route('/vet/session/add/health_record/<a_id>', methods=['GET', 'POST'], strict_slashes=False)
def add_health(a_id):
    """Add pet health record"""
    form = HealthRecordForm()
    vet = None
    appointment = []
    if session.get('vet_session', None) is not None:
        a_id = a_id
        appointment = Appointment.query.filter_by(a_id=a_id).first()
        pet_id = session['vet_session']
        vet_id = session['vet_id']
        vet = Vet.query.filter_by(vet_id=vet_id).first()
    else:
        flash('Warning: No vet session started! Start a vet session to add health record', 'error')
    if request.method == 'POST':
        if form.validate_on_submit():
            count_records = HealthRecord.query.filter_by(pet_id=pet_id).count()
            if count_records >= 12:
                old_records = HealthRecord.query.filter_by(pet_id=pet_id).all()
                for record in old_records:
                    db.session.delete(record)
                    db.session.commit()
            vet_doctor = form.vet_doctor.data
            date = datetime.now()
            symptoms = form.symptoms.data
            diagnosis = form.diagnosis.data
            treatment = form.treatment.data
            status = form.status.data
            health_record = HealthRecord(pet_id=pet_id, vet_id=vet_id, 
                                         vet_doctor=vet_doctor, date=date,
                                         symptoms=symptoms, diagnosis=diagnosis,
                                         treatment=treatment, status=status)
            db.session.add(health_record)
            db.session.commit()
            flash("Health record added successfully", 'success')
            return redirect(url_for('views.vet_session', pet_id=pet_id, a_id=a_id))
        flash('Error adding health record', 'error')
    return render_template('add_health.html', health_form=form, appointment=appointment, vet=vet)


@views.route('/vet/session/add/growth_record/<a_id>', methods=['GET', 'POST'], strict_slashes=False)
def add_growth(a_id):
    """Add pet growth record"""
    form = GrowthRecordForm()
    vet = None
    appointment = []
    if session.get('vet_session', None) is not None:
        a_id = a_id
        appointment = Appointment.query.filter_by(a_id=a_id).first()
        pet_id = session['vet_session']
        vet_id = session['vet_id']
        vet = Vet.query.filter_by(vet_id=vet_id).first()
    else:
        flash('Warning: No vet session started! Start a vet session to add growth record', 'error')
    if request.method == 'POST':
        if form.validate_on_submit():
            month = form.month.data
            year = form.year.data
            weight = form.weight.data
            height = form.height.data
            growth_record = GrowthRecord(pet_id=pet_id, vet_id=vet_id, month=month,
                                         year=year, weight=weight, height=height, vet_name=vet.name)
            db.session.add(growth_record)
            db.session.commit()
            flash("Growth record added successfully", 'success')
            return redirect(url_for('views.vet_session', pet_id=pet_id, a_id=a_id))
        flash('Error adding growth record', 'error')
    return render_template('add_growth.html', growth_form=form, appointment=appointment, vet=vet)