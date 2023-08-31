import os

#name = input("Please provide the file name\n")
oldName = os.path.basename(__file__)
#os.rename(oldName, name+".py")

X= "'Python' is most popular programming language"
print(X)
#To insert illegal string
print('Let\'s learn python')
#To insert TAB
print('Hello\tWorld!')
#use of string functions
dir(str)
#help(str.capitalize)
#print("sakil".capitalize())


#name = input("Please provide the number\n")
#reversed_name = name[::-1]
#print(reversed_name)

x= 12
y= 32

x,y = y,x

print("The value of x: ", x,
      "The Value of y: ", y)