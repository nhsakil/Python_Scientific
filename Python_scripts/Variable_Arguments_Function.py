"""
*args is used to iterate through function with keyword value
**kwargs is used to iterate through dunction with key value pairs
"""

def functionForIteratethrough(arg, *args):

    print(arg)
    for argument in args:
        print(f"Each value in arguments is {argument}")

functionForIteratethrough("12", "14", "sakil", "jhon", "54")

def keyValueArguments(**kwargs):
    for key, value in kwargs.items():
        print(f"key is {key} and value is {value}")

keyValueArguments(First = "4323", second = "Jhnon", Third = "Chucks")

def my_function(value1,value2, value3, value4):
    print(f"Value one is {value1}")
    print(f"Value two is {value2}")
    print(f"Value three is {value3}")
    print(f"Value four is {value4}")

values = ("43", "32", "54", "Jhon")
my_function(*values)

keyValues = {"value1":"32", "value2": "3243", "value3": "323", "value4": "Chucks"}
my_function(**keyValues)

def sumOfVariable(*args):
    sum = 0
    for value in args:
        sum = sum+int(value)
    return sum


values = ("23", "34", "43", "43")

total_sum = sumOfVariable(*values)
print(f"Total sum is {total_sum}")