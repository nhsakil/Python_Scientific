import numpy as np

arry = np.array([[1,2,3], [4,5,6]])
"""print(f"array: {arry}")
print(f"dimension of array: {arry.ndim}")
print(f"shape of array: {arry.shape}")
print(f"number of elements in array: {arry.size}")
print(f"data type of array: {arry.dtype}")"""

#accessing array elements
#row 1 coulmn 1
print(arry[0,0])
#2nd row all coulmns
print(arry[1,:])
# 1st and 2nd row, all coulmns
print(arry[0:2,:])
print(arry[:, 1:3])

