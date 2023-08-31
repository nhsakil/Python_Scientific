# dir (__builtins__)    erros functions

number = input("\nEnter radius for the circle\n")

try:
    number = int(number)
    print(f"Area of circle is {3.14*number}")

except ValueError:
    try:
        number = float(number)
        print(f"Area of circle is {3.14 * number}")

    except ValueError:
        print(f"opps, cannot convert {number} into numeric representation")
        print("Please enter a numaric value")
