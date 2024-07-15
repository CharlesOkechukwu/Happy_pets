import os
from flask import render_template, request, flash, redirect, url_for, current_app
from api import db
from api.views import views
from models import Pet
from werkzeug.utils import secure_filename
from datetime import date


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pet/add', methods=['GET', 'POST'], strict_slashes=False)
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
            pet.birth_date = date(birth_date)
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

def allowed_file(filename):
    """check if file is allowed"""
    allowed = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.split('.')[-1] in allowed

def upload_photo(file):
    """ulpload photo function"""
    upload_folder = os.path.join('static', 'uploads_img')
    current_app.config['UPLOAD'] = upload_folder
    filename = secure_filename(file.filename)
    if filename == '':
        flash("Upload pet's photo", 'error')
        return None
    else:
        if file and allowed_file(filename):
            file.save(os.path.join(current_app.config['UPLOAD'], filename))
            photo_path = os.path.join(current_app.config['UPLOAD'], filename)
        else:
            flash("File not allowed", 'error')
            return None
    return photo_path


@views.route('/health', methods=['GET'], strict_slashes=False)
def health():
    return render_template("health_tracker.html")

@views.route('/base')
def index():
    return render_template('base.html')