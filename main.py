#Number Guessing Game Objectives:
from art import logo
import random
import time
from replit import clear

guess1 = random.randint(0, 100)


def easy():
    attempts = 10
    while (attempts >= 1):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if (guess == guess1):
            print(f"You got it!!!The answer was {guess}.")
            break
        elif (guess > guess1):
            print("Too High")
            print("Guess Again")
        else:
            print("Too Low")
            print("Guess Again")
        attempts -= 1
        if (attempts == 0 and guess != guess1):
            print("You've run out of guesses, you lose.")
            break


def hard():
    attempts = 5
    while (attempts >= 1):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess : \n"))
        if (guess == guess1):
            print(f"You got it!!!The answer was {guess}.")
            break
        elif (guess > guess1):
            print("Too High")
            print("Guess Again")
        else:
            print("Too Low")
            print("Guess Again")
        attempts -= 1
        if (attempts == 0 and guess != guess1):
            print("You've run out of guesses, you lose.")
            break


def game_play():

    print("Welcome to the number guessing game .")
    print("I am thinking of a number between 1 and 100 .")
    print(f"psst, the correct number is {guess1}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' .\n")
    if (difficulty == 'easy'):
        easy()
    elif (difficulty == 'hard'):
        hard()
    else:
        print("Enter a proper Input !!!")


to_continue = 'y'
while to_continue == 'y':
    print(logo)
    game_play()
    time.sleep(5)

    clear()
    to_continue = input("Do you want to play the game ? Type 'y' or 'n' :\n")

print("Thank You")
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
