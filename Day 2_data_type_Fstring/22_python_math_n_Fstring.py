# 반올림
print(round(8 / 3)) # 값 : 3, 반올림. 소수점 첫째 자리(2.6)에서 반올림
print(round(8 / 3, 2)) # 값 : 2.67, 소수점 셋째 자리(2.666)에서 반올림

# 버림
print(8 / 3) # 2.6666666666666665, float, 실수
print(8 // 3) # 2, 버림(floor). int 정수

# 계속 연산
score = 0
score += 1 # score + 1 / +, -, *, /(나누기) 다 가능

print(score) # 1


# f-String

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# your score is 0, your height is 1.8, you are winning is True

