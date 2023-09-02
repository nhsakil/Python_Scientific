"""
With inheritance we get access to all method previous class and create new methods, here previous class is parent
class and new one is child class

"""

class Calculator:

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

#Inheritance of class object Calculator
class SuperCalculator(Calculator):
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a

myCalculator = SuperCalculator(34, 27)

temp = myCalculator.addition()
print(temp)

temp = myCalculator.subtraction()
print(temp)

temp = myCalculator.multification()
print(temp)

temp = myCalculator.division()
print(temp)

temp = myCalculator.cube(4)
print(temp)

temp = myCalculator.square(5)
print(temp)

#Method overriding in inheritance

class NewCalculator(Calculator):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def addition(self):
        return self.a +self.b+self.c

    def multification(self):
        return self.a*self.b*self.c
    def subtraction(self):
        return self.a -self.b

newCalculator = NewCalculator(32, 3, 4)

temp = newCalculator.addition()
print(temp)

temp = newCalculator.subtraction()
print(temp)

temp = newCalculator.multification()
print(temp)