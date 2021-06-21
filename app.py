# -*- coding: utf-8 -*-
#!/usr/bin/python3.9
################################################################################
##  Probability Mass Function for learning/hacking - Vintage 2021 Python 3.9  ##
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

__credits__ = {"credit1":"https://github.com/cardwizard/EllipticCurves/",
                "credit2":"https://github.com/yinengy/Mersenne-Twister-in-Python",
                "credit3":""}

###############################################################################
#                             Core Imports
###############################################################################
import math
import time
import numpy
import hashlib
import secrets
import numpy as np 
from flask import Flask
from binascii import hexlify
from matplotlib import pyplot as plt 

###############################################################################
#                              Local Imports
###############################################################################
from src.util.stats.ProbabilityMassFunction import MassProbabilityFunction as mpf
from src.util.Utils import errorprinter,GenPerpThreader
from src.util.Utils import modulo_multiply,modulo_pow
from src.primitives.EllipticalCurve import EllipticalCurve,Point
from src.util.stats.Entropy import Entropy


###############################################################################
#                      Flask Server / Flask Routes
###############################################################################
import os
import flask
import pickle
import numpy as np 
import pandas as pd 
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
	sayhello = TextAreaField('',[validators.DataRequired()])

class JupyterServer():
    '''Handler for Jupyter Notebooks to render them in the browser dynamically'''
    def __init__(self,filetoserve:str)->None:
        notebookconfig = '''
c.NotebookApp.allow_origin = '*' #Basic permission
c.NotebookApp.disable_check_xsrf = True #Otherwise Jupyter restricts you modifying the Iframed Notebook
c.NotebookApp.ip = 'ENTER_YOUR_JUPYTER_IP_ADDRESS' #Appears in the top browser bar when you launch jupyter
c.NotebookApp.port = 8888 #Your choice of port
c.NotebookApp.token = '' #In my case I didn't want to deal with security
c.NotebookApp.trust_xheaders = True #May or may not make a difference to you

c.NotebookApp.tornado_settings = {
'headers': {
'Content-Security-Policy': "frame-ancestors 'http://127.0.0.1:5000/' 'self' "
}
} #assuming your Flask localhost is 127.0.0.1:5000'''
    iframehtml = '''<iframe width="1000" height="1000"  src="http://ENTER_YOUR_JUPYTER_IP_ADDRESS:8888/notebooks/Desktop/test.ipynb"/>'''

class FlaskServer():
    '''Starts a flask server for a web interface'''
    def __init__(self,appname:str):

        app = Flask(appname)
        #self.runapp()

        @app.route("/stats")
        def encryption(self):
            return "Hello World!"

        @app.route("/ellipticalcurveplot")
        def plot(self):
            return "Hello World!"

        @app.route("/entropy")
        def stats(self):
            return "Hello World!"
        
        @app.route('/')
        def index(self):
            return flask.render_template('')

        def loadpickle(self,filename):
            loadedfile = pickle.load(open(filename,"r"))
            #@app.route('/'+ filename,methods = ['POST'])

        def writepickle(self,data):
            pass

        def output(self,filename):
            '''This is the function that outputs data to the browser screen
            feed it a filename'''
            if request.method == 'POST':
                app.render_template(filename+ '.html')
        
        def runapp(self)   :
            app.run(debug=True)

###############################################################################
#                       Plotting Elliptical Curves
###############################################################################
class PlotCurve():
    '''Plots an EllipticalCurve() with pyplot
>>> curve = EllipticalCurve(FieldSizeK:int ,a:int, b:int)'''
    def __init(self,CurveFunction:EllipticalCurve,
                    scaled = False, 
                    plotxmin = -128,
                    plotxmax =  128,
                    plotymin = -128,
                    plotymax =  128):
        # grab the information from the curve object            
        self.curve = CurveFunction
        self.x = self.curve.setofx
        self.y = self.curve.setofy
        #set plot boundries
        if scaled == True:
            raise NotImplementedError(message = "[-] Scaled plotting not implemented yet")
        elif scaled == False:
            self.plotxmin = plotxmin
            self.plotxmax = plotxmax
            self.plotymin = plotymin
            self.plotymax = plotymax
        #establish labels
        plt.title("Elliptical-Curve") 
        plt.xlabel("x")
        plt.ylabel("y") 
        #graph plot
        # x and y can be either an array, a list, or a single number
        # but sets of points must corellate by index
        # (x1,x2,x3),(y1,y2,y3) == (x1,y1),(x2,y2),(x3,y3)
        plt.plot(self.x,self.y) 
        plt.show()

###############################################################################
#                            Testing / Statistics
###############################################################################
class Test():
    def __init__(self):
        self.poolsize = 32 # numbers
        self.wordsize = 32 # bytes
        self.randompool = []
        self.poolofsha256randos = []

    def randombytes(self,bytesize):
        return secrets.token_bytes(bytesize)

    def randombytepool(self,poolsize,bytesize):
        '''fills a pool with random bytes'''
        self.randompool = []
        for i in range(poolsize):
            i=i
            self.randompool.append(self.randombytes(bytesize))
        return self.randompool

    def fillthepoolSHA256CounterMode(self,poolsize):
        '''fills a pool with sha256 hashes from a counter run to lim(x)'''
        for i in range(poolsize):
            herp = hashlib.sha256()
            herp.update(i)
            self.poolofsha256randos.append(herp.digest())
        return self.poolofsha256randos
    

    def TestEC(self)->None:
        e = EllipticalCurve(7, 3, 37)
        # # e.plot_curve().show()
        print(e)
        p = Point(e, 2, 5, "P")
        q = 4 * p

        q.name = "2P"
        e.plot_points([p, q])
        print(modulo_multiply(26, 19, 37))

    def runtest(self):
        print("[+] Initiating Test of the Entropy() Class")
        #asdf = self.randombytepool(32)
        #print(asdf)
        ent = Entropy(self.randombytepool(self.poolsize,self.wordsize))
        print("Entropy of a pool of {} sha256 hashes of the numbers 0-{}".format(self.poolsize,self.wordsize))
        print(ent.sigma())

        #asdf = self.randombytepool(32)
        #print(asdf)
        ent = Entropy(self.randombytepool(self.poolsize,self.wordsize))
        print("Entropy of a pool of {} real random {}-bit numbers".format(self.poolsize,self.wordsize))
        print(ent.sigma())


# I have no fucking idea what I am doing
#initiate statistics engine
test = Test()
test.runtest()