# -*- coding: utf-8 -*-
#!/usr/bin/python3.9
################################################################################
##            Distributed Point Function - Vintage 2021 Python 3.9            ##
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
__description__ = '''in cryptography, a distributed point function is a 
cryptographic primitive that allows two distributed processes to share a piece of
information, and compute functions of their shared information, without revealing
the information itself to either process. It is a form of secret sharing.

Given any two values a and b
one can define a point function
     Pa,b(x)  (a variant of the Kronecker delta function) 
     
     By:

    P a,b(x)={b for x=a 
             {0 for x≠a 

That is, it is zero everywhere 
    except at a 
    where its value is b


A distributed point function consists of a family of functions
    
    f(k) parameterized by keys k

and a method for deriving two:

    keys q and r 

from any two :
    
    input values a and b 

such that for all x:

    Pa,b(x)=fq(x)⊕fr(x)

where ⊕  denotes the bitwise exclusive or of the two function values. 
However, given only one of these two keys, 

the values of f 

for that key should be indistinguishable from random. 
'''
__url__ = '''https://en.wikipedia.org/wiki/Distributed_point_function'''
__docs__ = '''
'''