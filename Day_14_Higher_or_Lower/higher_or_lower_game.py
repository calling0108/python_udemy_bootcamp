from art import logo
from art import vs
from game_data import data
from replit import clear
import random


# logo print
def logo_image():
    print(logo)

# vs art print
def vs_image():
    print(vs)
    
# 임의의 경쟁 상대 도출 indexing을 위한 랜덤 함수 생성
def choice_player():
    number = random.randint(0, 49) # 전체 개수가 50개, len() 사용
    player = data[number] # random으로 뽑힌 수를 통해 player의 인덱스를 정해줌
    return player # return을 통해 choice_player() 함수의 값을 player로 반환함

# 경쟁 플레이어 선정
player_a = choice_player()
player_b = choice_player()

logo_image()

score = 0

should_continue = False

while not should_continue:
    print("Compare A: " + player_a["name"] + ", " + player_a["description"] + ", " + player_a["country"])
    print("A :" + str(player_a["follower_count"]))

    vs_image()

    print("Against B: " + player_b["name"] + ", " + player_b["description"] + ", " + player_b["country"])
    print("B :" + str(player_b["follower_count"]))

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    

    # A와 B의 Follower 수를 비교
    if player_a["follower_count"] < player_b["follower_count"]:
        if choice == "A":
            should_continue = True
            print(f"Sorry, that's wrong. Final score: {score}")
        elif choice == "B":
            score += 1
            clear()
            player_a = player_b
            player_b = choice_player()
            while player_b == player_a:
                player_b = choice_player()
            print(score)
            logo_image()
            print(f"You're right! Current score: {score}.")
    elif player_a["follower_count"] > player_b["follower_count"]:
        if choice == "A":
            score += 1
            clear()
            player_b = choice_player()
            while player_b == player_a:
                player_b = choice_player()
            print(score)
            logo_image()
            print(f"You're right! Current score: {score}.")
        elif choice == "B":
            should_continue = True
            print(f"Sorry, that's wrong. Final score: {score}")

