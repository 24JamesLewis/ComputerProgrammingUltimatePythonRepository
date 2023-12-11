import random
secret_number = random.randint(1, 10)
def number_guesser():
    number_guess = ""
    invalid_guess = True
    while invalid_guess == True:
        print("Guess a number from 1 - 10")
        number_guess = int(input())

        if number_guess == secret_number:
            print("You guessed correctly!")
            return invalid_guess == False     
        elif number_guess != secret_number:
            print("Try again!")
            invalid_guess == True    
       

number_guesser()


secret_number = random.randint(1, 10)
def number_guesser_with_lives():
    lives = 3
    number_guess = ""
    invalid_guess = True
    while invalid_guess == True:
        print("Guess a number from 1 - 10")
        number_guess = int(input())
        if lives == 1:
            print("Game over you lose!", "lives remaining:", lives - 1 )
            return invalid_guess == False and print("You lose!")

        elif number_guess == secret_number:
            print("You guessed correctly!", "You survived with:", lives)
            return invalid_guess == False
        elif number_guess != secret_number:
            lives = lives - 1
            print("Try again!", "Lives remaining:", lives )
            invalid_guess == True
            
number_guesser_with_lives()

def vending_machine(): 
    quarter = 25
    dime = 10
    nickel = 5
    due = 50
    coin_insert = ""
   
    while due > 0:
        print("Amount due:", due )
        print("Insert coin:")
        coin_insert = int(input())

        if coin_insert == quarter:
            due = due - quarter
        elif coin_insert == dime:
            due = due - dime
        elif coin_insert == nickel:
            due = due - nickel
    while due < 0:
        due = due * -1
        print("Change given:", due)
        return 

vending_machine()