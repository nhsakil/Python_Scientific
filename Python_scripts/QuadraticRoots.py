def solve_quadratic(a,b,c):
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
    root1, root2 = solve_quadratic(3,4,1)
    print(f"Roots: {root1} and {root2}")

