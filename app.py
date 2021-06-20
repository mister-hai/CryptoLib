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
import math
import time
import numpy
import hashlib
import secrets
import numpy as np 
from binascii import hexlify
from matplotlib import pyplot as plt 
from src.ProbabilityMassFunction import MassProbabilityFunction as mpf
from src.util.Utils import errorprinter,GenPerpThreader
from src.util.Utils import modulo_multiply,modulo_pow
from src.EllipticalCurve import EllipticalCurve,Point
from src.Entropy import Entropy

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
    
    def uniformity(self, x):
        '''Will return a number describing the uniformity of the data fed to it
    Accepts arrays of integers/floats'''
        return lambda x : 1 - 0.5*sum( abs(x - numpy.average(x)) )/(len(x)*numpy.average(x))
    
    def check_uniformity(self,setofprn):
        '''In statistics, the bias (or bias function) of an estimator is the 
    difference between this estimator's expected value and the true value of the
    parameter being estimated. An estimator or decision rule with zero bias is 
    called unbiased. In statistics, "bias" is an objective property of an estimator.
    Bias can also be measured with respect to the median, rather than the mean 
    (expected value), in which case one distinguishes median-unbiased from the 
    usual mean-unbiasedness property.'''
        uniformityarray = []
        for csprn in setofprn:
            # comparing csprn from pool to csprn after uniformity c
            #we have to compare each number for the distance between the values
            # we save the value representing the distance between the  two
            # in its own array and average those into one number, representing 
            # the bias, we want numbers close to 0?
            uniformityarray.append(self.uniformity(csprn))

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

from time import Timer
t = Timer()
test = Test()      # outside the try/except
try:
    t.timeit(test.runtest())    # or t.repeat(...)
except Exception:
    t.print_exc()
# I have no fucking idea what I am doing
#initiate statistics engine
#test = Test()
#test.runtest()