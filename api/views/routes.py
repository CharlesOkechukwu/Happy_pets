from flask import render_template
from api.views import views

@views.route('/')
def home():
    return render_template("home.html")