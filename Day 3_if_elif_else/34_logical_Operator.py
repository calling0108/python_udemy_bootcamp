"""
if condition1 & condition2 & condition3:
    do this
else:
    do this

A and B : A와 B 둘 다 '참'
C or D : C와 D 둘 중 하나가 '참'
not E : 조건에 반대로 결과를 만드는 것
"""

age = int(input("What's your age?: "))

if age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")

