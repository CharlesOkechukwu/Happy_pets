from flask import render_template
from api.views import views

@views.route('/')
def home():
    return render_template("service_dir.html")

@views.route('/pet', methods=['GET'], strict_slashes=False)
def get_pet():
    return render_template("add_pet.html")