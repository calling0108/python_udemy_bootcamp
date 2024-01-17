from art import logo
from art import vs
from game_data import data
from replit import clear
import random


# logo print
def logo():
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

# should_continue = False

# while not should_continue:
print("Compare A: " + player_a["name"] + ", " + player_a["description"] + ", " + player_a["country"])

vs_image()

print("Compare B: " + player_b["name"] + ", " + player_b["description"] + ", " + player_b["country"])

choice = input("Who has more followers? Type 'A' or 'B': ").upper()

# if choice == "A":
#     if player_a["follower_count"] < player_b["follower_count"]:
#         should_continue = True
# elif choice == "B":

    # 2개의 팔로워 수를 비교해야 함
    
        # 게임 종료
    #     should_continue = True
    # elif player_a["follower_count"] > player_b["follower_count"]:
    #     player_b = choice_player()