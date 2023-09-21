#numpy arrays are mutable
import numpy as np

arry = np.array([[1,2,3], [4,5,6]])
"""print(f"array: {arry}")
print(f"dimension of array: {arry.ndim}")
print(f"shape of array: {arry.shape}")
print(f"number of elements in array: {arry.size}")
print(f"data type of array: {arry.dtype}")"""

#accessing array elements
#row 1 coulmn 1
"""print(arry[0,0])
#2nd row all coulmns
print(arry[1,:])
# 1st and 2nd row, all coulmns
print(arry[0:2,:])
print(arry[:, 1:3])"""

#3x3 zero matrix

"""A = np.zeros((3,3))
print(f"array A: {A}")
B= A
B[0,0] = 1
print(f"copy of A: {B}")
print(f"array A:{A}")"""

"""x = np.arange(0,1,0.1)
print(f'equally spaced entries with increment 0.1: {x}')
y = np.linspace(0,3,6)
print(f'six equally spaced entries between 0 to 3: {x}')
#3x3 random array
R = np.random.random((3,3))
print(f"random matrix R: {R}")
#3x3 matrix with entries 1
W = np.ones((3,3))
print(f"Matrix W: {W}")
#3x3 identity matrix
I = np.eye(3)
print(f"identity matrix: {I}")
"""

"""#Some operations on arrays

A = np.array([[1,2,3], [4,5,6]])
print(f"2x3 A: {A}")
B = A.reshape((3,2))
print(f"2x3 reshaped to 3x2: {B}")
print(f"tranpose of A: {A.T}")

#Scaler multiple
print(f"3*A+5: {3*A+5}")
#Matrix product

print(f"A*B: {np.dot(A,B)}")
print(f"B*A: {np.dot(B,A)}")

#Vector Arithmatic
#Numpy automatically converts lists into vectors

u = [1,2,3]
v = [4,5,6]
print(f"innner product: {np.inner(u,v)}")
print(f"outer product: {np.outer(u,v)}")"""

#Reading and writing Numpy arrays into text file

A = np.random.random((3,3))
print(f"3x3 random matrix: {A}")
#save to text file
np.savetxt("random_array.txt",A)
#read from text file
B = np.loadtxt("random_array.txt")

print(f"loaded array: {B}")

# Create an array of numbers from 1 to 10
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate the sum, mean, and standard deviation
total_sum = np.sum(numbers)
mean_value = np.mean(numbers)
std_deviation = np.std(numbers)

# Print the results
print("Numbers:", numbers)
print("Sum:", total_sum)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)