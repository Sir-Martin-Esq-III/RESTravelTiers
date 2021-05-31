from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/<path:country>')
def retCountry(country):
     print(country)
     return render_template('index.html')