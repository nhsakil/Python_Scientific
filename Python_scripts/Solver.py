def quadroots(a, b, c=9):
    """
    Finding the root of quadritic equation ax**2+ bx + c = 0
    Input: coefficients a, b, c
    Output: Two real roots x1, x2
    """
    discriminant = b**2 - 4*a*c
    x1 = (-b +discriminant**.5)/(2*a)
    x2 = (-b - discriminant ** .5) / (2 * a)

    return x1, x2

def square(number):
    return number**2

import random

class RandomNumber:
    def randomNumber(number1, number2):
        return random.randint(number1, number2)
