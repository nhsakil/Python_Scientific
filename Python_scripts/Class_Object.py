"""
A function inside a class is called method
If a constructor is not defined then python called a constructor itself
Self is just reference of class instance
Class name should start with each capital letter (CamelCaps)
Attribute inside class is class attribute
Attribute inside object attribute
"""


class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multification(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "It's impossible to devide by zero"


# Create Object
myCalculator = Calculator()

temp = myCalculator.addition(12, 9)
print(temp)

temp = myCalculator.subtraction(24, 5)
print(temp)

temp = myCalculator.multification(23, 9)
print(temp)

temp = myCalculator.division(23, 0)
print(temp)


# To pass value inside class need to add constructor

class ConsCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multification(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "It's impossible to devide by zero"


CoCalculator = ConsCalculator(12, 6)

temp = CoCalculator.division()
print(temp)


class Polynomial():
    count = 0  # class attributes as it's variable is defined as inside class

    def __init__(self, coefficient):  # If a coefficient = 1 in inside the method then it's object attribute
        self.coeff = coefficient
        Polynomial.count += 1

    def degree(self):
        return len(self.coeff) - 1

    def __del__(self):
        Polynomial.count -= 1

    def evaluate(self, x):
        n = self.degree()
        sum = 0.
        for k in range(0, n + 1):
            sum += self.coeff[k] * x ** k
        return sum


print(f"Number of polynomials class before creation {Polynomial.count}")
myPolynomial = Polynomial([2, 3, 4])
print(myPolynomial.coeff)  # myPolynomial.coeff is a object attribute
print(myPolynomial.degree())
print(myPolynomial.evaluate(0))
print(f"Number of polynomials class after creation {Polynomial.count}")
del myPolynomial
print(f"Number of polynomials class after deletion {Polynomial.count}")
Polynomial.count = 5
print(f"Number of polynomials after setting value {Polynomial.count}")


class Rectangle:
    count = 0
    totalArea = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
        Rectangle.count += 1

    def area(self):
        Rectangle.totalArea += self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


print(f"Number of total rectangle before creation {Rectangle.count}")
myRectangle = Rectangle(4, 9)
print(f"Number of total rectangle after creation {Rectangle.count}")
myRectangle.area()
myRectangle1 = Rectangle(3, 3)
myRectangle1.area()
print(f"Total Area {Rectangle.totalArea}")


class MathUtils:

    def factorial(self, factorialDigit):
        self.number = factorialDigit
        sum = 1
        for number in range(1, factorialDigit):
            sum = sum + sum*number
        return sum


myFactorial = MathUtils()
myFactorial = myFactorial.factorial(6)
print(f"Factorial is {myFactorial}")
