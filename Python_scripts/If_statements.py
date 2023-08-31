principal = [10000,12000,23000, 3000, 32000, 2000, 5000]

if principal:
    print("Calculating the interests")
else:
    print("No accounts")

amount =[]

for balance in principal:
    if balance>10000:
        amount.append(balance+balance*0.05)
    else:
        amount.append(balance + balance * 0.02)
print(amount)


value = int(input("Please enter a number\n"))

if value >= 0:
    if value == 0:
        print("The value is zero")
    else:
        print("The value is positive")
else:
    print("The value is negative")