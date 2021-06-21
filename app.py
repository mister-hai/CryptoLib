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
from FlaskServer import FlaskServer
from test import Test
from JupyterServer import JupyterServer

import argparse
parser = argparse.ArgumentParser(description='Captive Portal tool')
parser.add_argument('--notebook',
                                 dest    = 'notebook',
                                 action  = "store" ,
                                 default = "/var/www/Cryptolib/notebook.ipynb", 
                                 help    = "Website to mirror, this is usually the only option you should set. Multiple downloads \
                                            will be stored in thier own directories, ready for hosting internally. " )
parser.add_argument('--wget_options',
                                 dest    = 'wget_options',
                                 action  = "store" ,
                                 default = "-nd -H -np -k -p -E" ,
                                 help    = "Wget options, Mirroring to a subdirectory is the default \n DEFAULT : -nd -H -np -k -p -E" )

def startjupyterserver():
    jupyterserver = JupyterServer("notebook.ipynb")
    jupyterserver.servenotebook()

def startflaskserver(self):
    flaskserver = FlaskServer("CryptoLib")
    flaskserver.runapp()

def starttest():
    # I have no fucking idea what I am doing
    #initiate statistics engine
    test = Test()
    test.runtest()