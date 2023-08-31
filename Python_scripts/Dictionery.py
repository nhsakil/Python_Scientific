Authors = ["Gilbert", "Second Author", "Third Author"]
Research_Books = {"Name": "Linear Algebra","Author":Authors, "Pages": 300}

print(Research_Books)
second_book = dict({"name": "Python for everybody", "author": "Charles"})
second_book["pages"] = 400
print(second_book)

del second_book["pages"]
print(second_book)

mapping_cities = {"Bangladesh": "Dhaka", "US": "New York", "UAE": "Dubai"}

country_name = input("Please enter your country name:\n")

for counrty in mapping_cities.keys():
    if counrty == country_name:
        print("Your city is ", mapping_cities[counrty])