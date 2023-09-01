def solve_quadratic(a,b,c=1):
    """
    Finding the roots of a quadratic equation ax^2 + bx + c = 0
    Input: Coefficients a,b, and c
    Output: Two real roots x1, x2
    Algorithm: quadratic formula
    """

    D= b**2 - 4*a*c
    X1 = (-b +D**0.5)/(2.*a)
    X2 = (-b - D ** 0.5) / (2. * a)
    return X1, X2

if __name__ == "__main__":

    print(solve_quadratic.__doc__)
    #Function calling with Positional arguments
    root1, root2 = solve_quadratic(3,4,1)
    print(f"Roots: {root1} and {root2}")

    #Function calling with key-value paris arguments

    a1=3
    b1 =4
    c1 = 1

    x1, x2 = solve_quadratic(c= c1  , a = a1, b = b1)
    print(f"Roots: {x1} and {x2}")

    #Function with default values

    x1, x2 = solve_quadratic(b=b1, a = a1)
    print(f"Roots: {x1} and {x2}")

def volumeOfRectangle(length, width, height):
    volume = length*width*height
    return volume

volume_of_box = volumeOfRectangle(length=23, height=13, width=12)
print(f"Volume of the box is {volume_of_box}")

