from app import app
from flask import render_template
from flask import abort
import json

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/<path:country>')
def retCountry(country):
     #Bit slow seeing as you have to open and read the whole file 
     try:
          with open('/Users/Thomas/Documents/Programming things/TravelTierAPI/RESTravelTiers/data.json') as json_file:
               data = json.load(json_file)
               return(data[country])
     except:
          abort(404)
