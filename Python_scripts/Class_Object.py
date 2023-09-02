"""
A function inside a class is called method
If a constructor is not defined then python called a constructor itself
Self is just reference of class instance
Class name should start with capital letter
"""
class Calculator:
    def addition(self, a, b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multification(self, a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "It's impossible to devide by zero"
#Create Object
myCalculator = Calculator()

temp = myCalculator.addition(12,9)
print(temp)

temp = myCalculator.subtraction(24,5)
print(temp)

temp = myCalculator.multification(23,9)
print(temp)

temp = myCalculator.division(23,0)
print(temp)

#To pass value inside class need to add constructor

class ConsCalculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a - self.b
    def multification(self):
        return self.a*self.b
    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return "It's impossible to devide by zero"

CoCalculator = ConsCalculator(12,6)

temp = CoCalculator.division()
print(temp)