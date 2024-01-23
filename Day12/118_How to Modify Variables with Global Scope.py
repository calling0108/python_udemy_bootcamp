# enemies = 1

# def increase_enemies():
#     global enemies # 전역 변수 선언, 그러나 버그와 오류 문제로 추천하지 않음, 수정이 까다로움.
#     enemies += 1 
#     print(f"enemies inside function: {enemies}") # 2

# increase_enemies()
# print(f"enemies outside function: {enemies}") # 1

# 다른 방법

enemies = 1

def increase_enemies(): 
    print(f"1_enemies outside function: {enemies}")
    return enemies + 1 # 전역 변수 선언이 아닌, 함수를 만들어서 활용하면 됨.

enemies = increase_enemies()
print(f"enemies outside function: {enemies}") # 2

while enemies < 5:
    increase_enemies()
    enemies = increase_enemies()
    print(enemies)