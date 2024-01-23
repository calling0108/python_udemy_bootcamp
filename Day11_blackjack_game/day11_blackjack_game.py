import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# start_game = False

# if play_game == "y":
#     print(logo)
# elif play_game == "n":
#     start_game = True

# 카드 뽑기
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def double_deal():
    choiced_card = []
    for i in range(0, 2):
        new_card = deal_card()
        choiced_card.append(new_card)
    return choiced_card

user_choice_card = double_deal()
computer_choice_card = double_deal()

computer_first_card = computer_choice_card[0]
computer_second_card = computer_choice_card[1]

print(computer_first_card)
print(computer_second_card)


print(f"Your cards: {user_choice_card}")
print(f"computer cards: {computer_choice_card}")

# blackjack 확인
ten_cards = random.choice(cards[9:12])


if user_choice_card == 11 and ten_cards:
    if computer_choice_card == 11 and ten_cards:
        print("draw")
    print("User Win")
# 블랙잭 찾기, cards[0]과 cards[9:12]가 중복되면 블랙잭으로 승리!

should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

if should_continue == "y":
    # user 다른 카드 추가
elif should_continue == 'n':
    print(computer_choice_card)
    # user와 pc의 카드합을 비교, 조건문 진행, 게임 결과 출력, 재게임 진행 여부 묻기
    if 




