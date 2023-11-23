from art import logo
import random

def draw_card():
    u1_card = random.choice(card_list) 
    u2_card = random.choice(card_list)
    p1_card = random.choice(card_list)

    print(f"Your cards: [{u1_card}, {u2_card} ]current score: {u1_card + u2_card}")
    print(f"Computer's first card: {p1_card}")

start_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start_answer == "y":
    print(logo)




card_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

a = False

while not a: # user 카드 뽑기 과정 반복
    
    
    keep_game = input("Type 'y' to get another card, type 'n' to pass: ")

if keep_game == "n":
    print("yes")