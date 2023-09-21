import numpy as np
from scipy.linalg import solve
from scipy import linalg

# Define the coefficient matrix (A) and the constant matrix (b)
# Example system of linear equations:
# 2x + y = 5
# 3x - 2y = -8
# This corresponds to the matrices:
# A = [[2, 1],
#      [3, -2]]
# b = [5, -8]
A = np.array([[2, 1],
              [3, -2]])

b = np.array([5, -8])

# Solve the system of linear equations
solution = solve(A, b)

# Print the solution
print("Solution:")
print("x =", solution[0])
print("y =", solution[1])

A = np.array([[3,2,0],[1,-1,0],[0,5,1]])
b = np.array([2,4,-1])
x = solve(A,b)
print(f"x: {x}")
print(np.dot(A,x)==b)