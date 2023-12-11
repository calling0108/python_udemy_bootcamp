#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print("Welcom to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer_number = random.randint(1, 101)
print(answer_number)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "hard":
    print("You have 5 attempts remaining to guess the number.")
if level == "easy":
    print("You have 10 attempts remaining to guess the number.")

def lose_life():
    if answer_number == "hard":
        life = 5
    else:
        life = 10
    return

guess_number = int(input("Make a guess: "))

if guess_number > answer_number:
    print("Too high.")
    print("Guess again.")
elif guess_number < answer_number:
    print("Too low.")
    print("Guess again.")
else:
    print(f"You got it! The answer was {answer_number}")

