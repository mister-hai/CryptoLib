# -*- coding: utf-8 -*-
#!/usr/bin/python3.9
################################################################################
##         Crypto code for learning/hacking - Vintage 2021 Python 3.9         ##
################################################################################                
# Licenced under GPLv3-modified                                               ##
# https://www.gnu.org/licenses/gpl-3.0.en.html                                ##
#                                                                             ##
# The above copyright notice and this permission notice shall be included in  ##
# all copies or substantial portions of the Software.                         ##
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

__credits__ = {"credit1":"mister-hai",
                "credit2":"https://github.com/yinengy/Mersenne-Twister-in-Python",
                "credit3":""}

###############################################################################
#                             Core Imports
###############################################################################
import os,sys
from flask_wtf.csrf import CSRFProtect

from app.test import Test
from app.FlaskServer import FlaskServer
from app.JupyterServer import JupyterServer
from app.src.util.Utils import greenprint,redprint,blueprint,errorprinter
from app.src.primitives.EllipticalCurve import EllipticalCurve,Point

import argparse
parser = argparse.ArgumentParser(description='CryptoLib Test and Learning Platform')
parser.add_argument('--notebook',
                                 dest    = 'notebook',
                                 action  = "store" ,
                                 default = "/var/www/Cryptolib/notebook.ipynb", 
                                 help    = "Jupyter Notebook File to serve" )
parser.add_argument('--flask-ip',
                                 dest    = 'flaskipaddr',
                                 action  = "store" ,
                                 default = "127.0.0.1" ,
                                 help    = "IP Address of the flask server" )
###############################################################################
#                           Flask Server
###############################################################################
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

class FalskSwerver(FlaskServer):
    app = None
    def __init__(self, appname:str,
                notebooktoserve:str,
                jupyteripaddr:str,
                jupyterport:str):
        self.notebooktoserve = notebooktoserve
        self.jupyterport = jupyterport
        self.jupyteripaddr = jupyteripaddr
        app = Flask(appname)
        csrf = CSRFProtect(app)
        self.runapp(app)
        self.test = self.starttest()
    
    @app.route("/ellipticalcurveplot")
    def plot(self):
        form = PlotInputForm(request.form)
        #this is how you retrieve form field data
        x1 = request.form['x1']
        x2 = request.form['x2']
        a = request.form['a']
        b = request.form['b']
        self.test.TestEC(x1,a,b)
        app.render_template('ellipticalcurveplotting.html', form=form)

    @app.route('/notebook', methods=['GET','POST'])
    def notebook(self):
        '''Starts a jupyter server'''
        if request.method == 'POST' :#and form.validate():
            notebook = JupyterServer(self.notebooktoserve,
                                     self.jupyteripaddr,
                                     self.jupyterport,
                                     self.flaskport,
                                     self.flaskipaddr)
            notebookrender = notebook.iframehtml
        return notebookrender

    @app.route("/stats")
    def encryption(self):
        return ""

    def startjupyterserver(self):
        jupyterserver = JupyterServer("notebook.ipynb")
        jupyterserver.servenotebook()

def startflaskserver(self):
    # still use a CSRF despite it being local development mode
    # you know know!
    os.environ['WTF_CSRF_SECRET_KEY'] = 'a random string'
    os.environ['FLASK_ENV'] = "development"
    flaskserver = FlaskServer("CryptoLib")
    flaskserver.runapp()

def starttest():
    # I have no fucking idea what I am doing
    #initiate statistics engine
    greenprint("[+] Running Test!")
    test = Test()
    test.runtest()
    return test

if __name__ == "__main__":
    greenprint("[+] Parsing Command Line Arguments")
    arguments  = parser.parse_args()