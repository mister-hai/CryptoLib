###############################################################################
#                             Core Imports
###############################################################################
import math
import numpy
from matplotlib import pyplot as plt 
###############################################################################
#                              Local Imports
###############################################################################
from app.src.util.Utils import modulo_multiply,modulo_pow,randombytepool
from app.src.primitives.EllipticalCurve import EllipticalCurve,Point
from app.src.util.stats.Entropy import Entropy

###############################################################################
#                            Testing / Statistics
###############################################################################
class Test():
    def __init__(self):
        self.poolsize = 32 # numbers
        self.wordsize = 32 # bytes
        self.randompool = []
        self.poolofsha256randos = []

    def TestEC(self)->None:
        e = EllipticalCurve(7, 3, 37)
        # # e.plot_curve().show()
        print(e)
        p = Point(e, 2, 5, "P")
        q = 4 * p

        q.name = "2P"
        e.plot_points([p, q])
        return (modulo_multiply(26, 19, 37))

    def runtest(self):
        print("[+] Initiating Test of the Entropy() Class")
        #asdf = self.randombytepool(32)
        #print(asdf)
        ent = Entropy(randombytepool(self.poolsize,self.wordsize))
        print("Entropy of a pool of {} sha256 hashes of the numbers 0-{}".format(self.poolsize,self.wordsize))
        print(ent.sigma())

        #asdf = self.randombytepool(32)
        #print(asdf)
        ent = Entropy(randombytepool(self.poolsize,self.wordsize))
        print("Entropy of a pool of {} real random {}-bit numbers".format(self.poolsize,self.wordsize))
        print(ent.sigma())
