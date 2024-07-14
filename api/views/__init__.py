#!/usr/bin/python3
"""Create a Blueprint for routes"""

from flask import Blueprint, render_template, url_for, redirect

views = Blueprint('views', __name__)

# Import routes to register with the Blueprint
from api.views import routes