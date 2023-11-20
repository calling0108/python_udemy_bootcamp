import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card

def double_deal():
    choiced_card = [] # ex) [5, 8]
    for i in range(0, 2):
        choiced_card.append(deal_card())
    return choiced_card

user_choice_card = double_deal()
user_choice_card += deal_card()
computer_choice_card = double_deal()

computer_first_card = computer_choice_card[0]
computer_second_card = computer_choice_card[1]

print(logo)

print(f"Your cards: {user_choice_card}")
print(f"computer cards: {computer_first_card}")

# Blackjack confirm


