
prompt = "\nEnter a positive number to check if it's prime"
prompt += "\n(Enter -1 when you are done.)\n"

while True:
    num = int(input(prompt))

    if num == -1:
        break
    else:
        temp = 0
        for i in range(2,num):
            if num % i ==0:
                print(f"{num} = {i}*{num//i}")
                break
            temp = i
        if temp == num -1:
            print(f"{num} is a prime number")