import Solver   # import entire modeule
import Solver as sol    # import entire module and give it alternate name (alias)
from Solver import quadroots as root    #import a specific function from module

a1 = 1
b1 = 0

roots = sol.quadroots(c= 16, a= a1, b = b1)

print(roots)

from Solver import square

squareofNumber1 = square(3)
squareofNumber2 = square(45)
squareofNumber3 = square(32)

print(squareofNumber1, squareofNumber2, squareofNumber3)

from Objects_as_Attribbutes import Polynomial, Monomial

qadpoly = Polynomial([1,2,3,4])

print("Lead term of quadpoly: ")
qadpoly.leading_term.property()

mono = Monomial()
print("Monomial: ")
mono.property()

import math

b= math.exp(1)
b= math.cos(math.pi/3)

from Solver import RandomNumber

minVAlue = 1
maxValue =34

randomNumber1 = RandomNumber.randomNumber(minVAlue, maxValue)
randomNumber2 = RandomNumber.randomNumber(minVAlue, maxValue)

print(f"Random number 1: {randomNumber1}, Random number 2: {randomNumber2}")
