
#!/usr/bin/python3
"""Create a Blueprint for routes for auth"""

from flask import Blueprint, render_template, url_for, redirect

auth = Blueprint('auth', __name__)
from api.auth import routes
from .utils import hash_password
from api.auth import auth