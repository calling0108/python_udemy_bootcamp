# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)

# if, while, for와 같이 콜론과 들여 쓰기가 있는 모든 코드 블록은 지역 범위를 만드는 것으로 간주되지 않는다.


enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)