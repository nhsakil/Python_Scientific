import math
class Polynomial:
    """ A class of polynomials (Base class)"""

    def __init__(self, coefficient):
        """Initialize  the coefficient attributes"""
        self.coeff = coefficient
    def degree(self):
        """Find the degree of polynomial"""
        return len(self.coeff) - 1
class Quadratic(Polynomial):
    """A class quadratic polynomials ( inherits from Polynomial class)"""
    def __init__(self, coefficient,power_increase):
        self.power_increase = power_increase
        super().__init__(coefficient)
    def roots(self):
        c= self.coeff[0]
        b= self.coeff[1]
        a = self.coeff[2]

        if self.power_increase == -1:
            a = self.coeff[0]
            c = self.coeff[2]
        discriminant = b**2 - 4*a*c
        r1 = (-b + discriminant**0.5)/(2*a)
        r2 = (-b - discriminant ** 0.5) /(2 * a)
        return r1, r2
    def degree(self):
        return 2

quadpoly1 = Quadratic([2,-3,1],1)
print(f"roots: {quadpoly1.roots()}")

quadpoly2 = Quadratic([2,-3,1],1)
print(f"roots: {quadpoly2.roots()}")

poly = Polynomial([2,-3,1,0])
print(f"Degree: {poly.degree()}")

quadPoly = Quadratic([2,-3,1],0)
print(f"Degree: {quadPoly.degree()}")

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*4*self.radius**2

rectangle = Rectangle(6,7)
triangle = Triangle(34,2)
circle = Circle(6)

print(f"Area of rectangle: {rectangle.area()}")
print(f"Area of triangle: {triangle.area()}")
print(f"Area of circle: {circle.area()}")

