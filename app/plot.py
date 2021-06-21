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
from app.src.util.stats.ProbabilityMassFunction import MassProbabilityFunction as mpf
from app.util.Utils import errorprinter,GenPerpThreader
from app.src.util.Utils import modulo_multiply,modulo_pow
from app.src.primitives.EllipticalCurve import EllipticalCurve,Point
from app.src.util.stats.Entropy import Entropy

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
