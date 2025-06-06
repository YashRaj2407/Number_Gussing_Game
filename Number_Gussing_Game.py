import random

def number_gussing_game():
    number_to_guess =random.randint(1,100)
    guess=None
    tries=0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking a number between 1 to 100.")

    while guess != number_to_guess:
        try:
            guess=int(input("Enter your guess: "))
            tries +=1
            if guess < number_to_guess:
                print("Too Low! Try again.")
            elif guess > number_to_guess:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed it in {tries} tries.")
        except ValueError:
            print("Enter a valid number.")
number_gussing_game()




    