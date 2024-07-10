from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """render home page"""
    return render_template('health_tracker.html')


if __name__ == '__main__':
    app.run(debug=True)