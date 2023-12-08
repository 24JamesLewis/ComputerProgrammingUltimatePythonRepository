import random
number = random.randint(1, 10)
def number_guesser():

    number_guess = ""
    invalid_guess = True
    while invalid_guess == True:
        print("Guess a number from 1 to 10")
        number_guess = input()
        if number_guess > number:
            print("Your guess was too high")
        elif number_guess < number:
            print("Your guess was too low")

        if number_guess is number:
            invalid_guess == False
print(random.randint(1, 10))
number_guesser()