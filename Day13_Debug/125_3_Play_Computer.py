# Play Computer
# 컴퓨터의 입장(컴퓨터처럼)에서 생각하기 

year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# elif year > 1994:
elif year >= 1994: # 1994년을 포함해서 계산하도록 하기
  print("You are a Gen Z.")