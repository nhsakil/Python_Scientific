# dir (__builtins__)    erros functions

number = input("\nEnter a number\n")

try:
    number = int(number)
    print(f"you entered {number} which is a integer")

except ValueError:
    try:
        number = float(number)
        print(f"You entered {number} which is a float")
    except ValueError:
        print(f"opps, cannot convert {number} into numeric representation")
        print("Please enter numaric value")
