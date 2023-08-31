mixed_list = [1,2,"item 1","8", 3,6]
mixed_list[3] = int(mixed_list[3])

#Slicing a list, upper bound index is excluded

sliced_list = mixed_list[2:4]

print(sliced_list)
print(mixed_list[:3])   # Indices sliced(0,1,2)
print(mixed_list[:4])   # Indices sliced(0,1,2,3)

#Creating numaric list with range
range_list = list(range(-27,67,10))
print(range_list)

# Immutable list that can't be change - tuple
space_dimension = (1,2,3,4)


# Print even numbers from a list


even_list = list()

for number in list(range(1,20)):
    if (number%2) == 0:
      even_list.append(number)

print("The sum of even numbers: ", sum(even_list))