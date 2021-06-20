# -*- coding: utf-8 -*-
#!/usr/bin/python3.9
################################################################################
##       Elliptic Curve for learning/hacking - Vintage 2021 Python 3.9        ##
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
__description__ = '''Calculates An eliptic curve function
https://en.wikipedia.org/wiki/One-way_compression_function
'''
__url__ = '''https://en.wikipedia.org/wiki/One-way_compression_function'''
__docs__ = '''
The population count of a bitstring is often needed in cryptography and other 
applications. The Hamming distance of two words A and B can be calculated as 
the Hamming weight of A xor B.[1]

The problem of how to implement it efficiently has been widely studied. A 
single operation for the calculation, or parallel operations on bit vectors
are available on some processors. For processors lacking those features, the
best solutions known are based on adding counts in a tree pattern. 

For example, to count the number of 1 bits in 

    16-bit binary number a = 0110 1100 1011 1010, 

these operations can be done: 


Here, the operations are as in C programming language, so X >> Y means to shift X right by Y bits, X & Y means the bitwise AND of X and Y, and + is ordinary addition. The best algorithms known for this problem are based on the concept illustrated above and are given here:[1] 
'''

class HammingWeight():
    def __init(self,byteinput)->None:
        self.input = byteinput
        self.inputbinary = b''
        pass
    
    def bitcounter1(self,byteitem, wordsize):
        '''uses sum() and bit operations in a loop'''
        for i in range(wordsize):
            bits = [].append( byteitem & (1 << i) > 0 )
            return sum(bits)

    def bitcounter2(self, byteitem):
        '''uses bit operations in a loop'''
        counter = 0
        for index in byteitem:
            byteitem &= (byteitem - 1)
            counter += 1
        return counter

    def bitcounter3(self):
        '''converts the byte to a b'0101010' string and counts the 1's
using text processing and not math'''
        pass
