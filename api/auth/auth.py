from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/Add a Pet')
def pet():
    return render_template('add a pet')

# main.py (Main Flask app file)
from flask import Flask
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/chat')
def chat():
    return "Chat with us page"

if __name__ == '__main__':
    app.run(debug=True)
    