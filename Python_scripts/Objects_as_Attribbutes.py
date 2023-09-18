class Monomial():

    def __init__(self, a=1,n=0):
        self.a = a
        self.n = n

    def property(self):
        if self.a > 0:
            print("positive coefficient: ", self.a)
        if self.a < 0:
            print("negative coefficient: ", self.a)
        if self.a == 0:
            print("zero coefficient: ", self.a)
        if self.n%2 == 0:
            print("even power: ", self.n)
        else:
            print("odd power: ", self.n)

class Polynomial():

    def __init__(self, coefficient):
        self.coeff = coefficient
        n = len(coefficient)
        a = coefficient[-1]
        self.leading_term = Monomial(a,n)   #attribute leading term is a monomial object

class Quadratic(Polynomial):

    def __init__(self, coefficient, power_increase):
        super().__init__(coefficient)
        self.power_increase = power_increase
        self.leading_term = Monomial(coefficient[2],2)
        if power_increase == -1:
            self.leading_term = Monomial(coefficient[0], 2)

mono = Monomial()
print(f"default monomial : {mono.property()}")

poly = Polynomial([1,2,3,4,5])
print(f"leading term of polynomial: {poly.leading_term.property()}")

qaudpoly = Quadratic([1,2,3],1)
print(f"leading term of quadratic polynomial: {qaudpoly.leading_term.property()}")

qaudpoly = Quadratic([1,2,3],-1)
print(f"leading term of quadratic polynomial: {qaudpoly.leading_term.property()}")
