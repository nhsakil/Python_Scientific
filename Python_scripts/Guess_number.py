import random

lower_number = 1
upper_number = 100
numer_of_guess = 0

random_numer = random.randint(lower_number, upper_number)

guess =int(input("Guess the number: "))

while guess != random_numer:
    if guess < random_numer:
        print("The number is higher")
    else:
        print("The number is lower")
    numer_of_guess += 1
    guess = int(input("Guess the number: "))
print(f"Congratulations! You guessed the number correctly in {numer_of_guess} attempts")
