"""
An immutable object can't change it's value or content after creation. Built in types- float, string, int, tuple, bool
A mutable object can change it's value or content after creation. Built in types- dictionery, list, set
Calling function with mutable parameter is called pass-by-value model
Python uses pass-by-object-reference model to pass mutable object
"""

def pass_by_value(x):
    x=5
    print(f"Inside the function x = {x}")

x= 3
print(f"Before calling function x = {x}")
pass_by_value(x)
print(f"After the calling function x= {x}")

def pass_by_reference(list_received):
    list_received[0] =1
    list_received.append(2)

list_sent = [0]
print(f"Before the call function list = {list_sent}")
pass_by_reference(list_sent)
print(f"After calling the function list = {list_sent}")

def pass_by_value_reference(a,b,argumentlist):
    if a and b is not None:
        argumentlist[0] = 4
        argumentlist.append(8)

sentArgumentList = [1]

print(f"Value bofore calling function {sentArgumentList}")
pass_by_value_reference(1,2,sentArgumentList)
print(f"Value after calling function {sentArgumentList}")
