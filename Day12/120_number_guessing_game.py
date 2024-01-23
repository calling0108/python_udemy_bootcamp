# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

# logo 메시지 출력
print(logo)

# 환영인사~~~ 환잉~~
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer_number = random.randint(1, 100)

# 정답 숫자 확인
# print(answer_number)

# 난이도 선택
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "hard":
    print("You have 5 attempts remaining to guess the number.")
    life = 5
if level == "easy":
    print("You have 10 attempts remaining to guess the number.")
    life = 10

# 생명 잃게
def lose_life():
    # 전역변수 설정
    global life
    life -= 1

should_continue = True

while should_continue:
    guess_number = int(input("Make a guess: "))

    if guess_number == answer_number:
        print(f"You got it! The answer was {answer_number}")
        should_continue = False
    elif guess_number != answer_number:
        if guess_number > answer_number:
            print("Too high.")
        elif guess_number < answer_number:
            print("Too low.")
        
        lose_life()

        if life == 0:
            should_continue = False
            print("You've run out of guesses, you lose.")
        elif life != 0:
            print("Guess again.")
            print(f"You havce {life} attempts remaining to guess the number.")



# Answer
            

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
