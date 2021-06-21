
###############################################################################
#                Flask Server / Flask Routes / User Interface
###############################################################################
import os
import flask
import pickle
import numpy as np 
import pandas as pd 
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, Response,request
from wtforms import Form, TextAreaField, validators, StringField
from wtforms.validators import DataRequired

#wtforms stuff
class PlotInputForm(Form):
    plotinput = TextAreaField('',[validators.DataRequired()])
#example for reference
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response

class FlaskServer():
    '''Starts a flask server for a web interface'''
    app = None
    def __init__(self,appname:str,
                      flaskport:str, 
                      flaskipaddr:str)->None:
        self.flaskport = flaskport
        self.flaskipaddr = flaskipaddr
        

    def output(self,filename):
        '''This is the function that outputs data to the browser screen
        feed it a filename'''
        if request.method == 'POST':
            render_template(filename+ '.html')
        
    def runapp(self, app):
        app.run(debug=True)

    @app.route('/')
    def index(self):
        return flask.render_template('')

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))
