#To create infinite loop until it become false
# TO stop infinte loop (cntrl+c)

x = 1

while x**3 <= 9999:
    x += 1
    #print(f"x = {x}, x**3 = {x**3}")
x -= 1
print(f"The maximum integer number whose cube is <= 9999 : {x}, x**3 = {x**3}")