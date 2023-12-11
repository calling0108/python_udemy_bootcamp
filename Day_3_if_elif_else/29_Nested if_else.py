"""
if condition 1:
    if another condition 1-1: # con1 조건도 참, con 1-1 조건 참
        do A
    elif condition 1-2: # con1 조건 참, con 1-1 조건 거짓
        do B
    else: # con 1 조건 참, con 1-1, 1-2 조건은 거짓
        do this
else: # 상단 if 조건이 거짓
    do this
"""

height = int(input("What is your height in cm? "))

if height > 120:
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
elif height == 120:
    print("sala sala")
else:
    print("Hi")