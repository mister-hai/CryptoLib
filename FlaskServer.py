
###############################################################################
#                Flask Server / Flask Routes / User Interface
###############################################################################
import os
import flask
import pickle
import numpy as np 
import pandas as pd 
from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators, StringField
from wtforms.validators import DataRequired
#wtforms stuff
class PlotInputForm(Form):
    plotinput = TextAreaField('',[validators.DataRequired()])
#example for reference
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class FlaskServer():
    '''Starts a flask server for a web interface'''
    app = None
    def __init__(self,appname:str):
        app = Flask(appname)
        self.runapp()

    def output(self,filename):
        '''This is the function that outputs data to the browser screen
        feed it a filename'''
        if request.method == 'POST':
            render_template(filename+ '.html')
        
    def runapp(self)   :
        self.app.run(debug=True)

    @app.route('/plotting', methods=['GET','POST'])
    def plotting(self):
        if request.method == 'POST' :#and form.validate():
            return render_template('plotting.html')

    @app.route("/stats")
    def encryption(self):
        return "Hello World!"

    @app.route("/ellipticalcurveplot")
    def plot(self):
        form = PlotInputForm(request.form)
        #this is how you retrieve form field data
        x1 = request.form['x1']
        x2 = request.form['x2']
        a = request.form['a']
        b = request.form['b']
        return render_template('ellipticalcurveplotting.html', form=form)

    @app.route("/entropy")
    def stats(self):
        return "Hello World!"
        
    @app.route('/')
    def index(self):
        return flask.render_template('')

    #def loadpickle(self,filename):
    #    loadedfile = pickle.load(open(filename,"r"))
    #    @app.route('/'+ filename,methods = ['POST'])

    #def writepickle(self,data):
    #    pass
