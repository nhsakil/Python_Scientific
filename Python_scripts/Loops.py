#Nested loops

A= [[0,0,0],[0,0,0],[0,0,0]]    # 3*3 matrix using nested loops

for i in range(0,3):
    for j in range(0,3):
        A[i][j] = 1/(i+j+1)

print(A)
print(A[0])
print(A[2][2])

#loop through dictionery
methods = {"root": "Newton", "interpolation": "lagrance", "integreation": "simson"}

#loop through key-value pairs

for prob, method in methods.items():
    print("key= " + prob + ", Value= " + method)

#loop through keys

for prob in methods.keys():
    print("key= " + prob)

#loop through values
for method in methods.values():
    print("value= " + method)

x= 10
sum = 1
for i in range(1,x+1):
    sum = sum*i
#print("Factorial of "+ str(x) +" "+ sum)
print("{}{}{}{}".format("Factorial of ",x," is ",sum))