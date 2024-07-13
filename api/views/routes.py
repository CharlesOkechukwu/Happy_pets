from flask import render_template, request
from api.views import views

@views.route('/')
def home():
    return render_template("service_dir.html")

@views.route('/pet', methods=['GET', ], strict_slashes=False)
def get_pet():
    if request.method == 'POST':
        name = request.form.get('name')
        specie = request.form.get('specie')
        breed = request.form.get('breed')
        age = request.form.get('age')
        color = request.form.get('color')
        
    return render_template("add_pet.html")

@views.route('/health', methods=['GET'], strict_slashes=False)
def health():
    return render_template("health_tracker.html")

@views.route('/base')
def index():
    return render_template('base.html')