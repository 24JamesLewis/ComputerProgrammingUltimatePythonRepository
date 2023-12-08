import random
secret_number = random.randint(1, 10)
def number_guesser():
    number_guess = ""
    invalid_guess = True
    while invalid_guess == True:
        print("Guess a number from 1 - 10")
        number_guess = input()
        if number_guess == secret_number:
            invalid_guess == False and print("You guessed correctly")
        elif number_guess != secret_number:
            invalid_guess == True and print("Try again!")
            
print(secret_number)
number_guesser()