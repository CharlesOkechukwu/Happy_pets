#!/usr/bin/python3
# Other functions

# Imports
import os
from flask import current_app, flash
from werkzeug.utils import secure_filename

def allowed_file(filename):
    """check if file is allowed"""
    allowed = ['png', 'jpg', 'jpeg', 'JPG', 'jfif']
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
