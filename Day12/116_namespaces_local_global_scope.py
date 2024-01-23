################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}") # 1



# Local Scope 지역 변수

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength -> name error 발생

# Global Scope 전역 변수

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health) 

drink_potion() # 10, 전역 변수
print(player_health) # 10, 전역 변수


def game():
    def drink_potion_2():
        potion_strength = 2 
        print(player_health) 

    drink_potion_2() # game 함수 내 drink_potion을 실행시키기 위함

print(player_health)
