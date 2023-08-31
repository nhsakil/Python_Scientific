prompt = "\nEnter numbers to sum"
prompt += "\n(Enter 0 when you are done.)\n"

temp = list()

while True:
    try:
        num =int(input(prompt))
        if num == 0:
            break
        else:
            temp.append(num)
    except:
        print("Please enter only numbers")

print(f"The sum of total {len(temp)} numbers is {sum(temp)}")
