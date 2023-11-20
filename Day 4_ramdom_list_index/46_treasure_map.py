line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#  ME

# ex) position == A3:

# A와 3을 따로 분리 -> 리스트화
list_position = list(position) # list_position = ['A', '3'] 

# A와 3을 인덱싱 해주기
# a = 0
# b = 1
# c = 2

# 1 = 0
# 2 = 1
# 3 = 3

# ANSWER

letter = position[0].lower() # a, b, c의 결과값
abc = ["a", "b", "c"] # 문자의 인덱스를 숫자로 변경시키기 위해 input값을 상정해놓음
letter_index = abc.index(letter) # valuable.indes("letter")는 해당 변수 내에 있는 문자(letter)의 index를 출력해준다
number_index = int(position[1]) - 1 # index는 0부터 세기 시작하기 때문에 항상 -1을 해주어야 한다
map[number_index][letter_index] = "X" # map 변수에 line1~3 list가 중첩되어 있음. number_index가 line1~3으로 시작하는 값을 정하므로 앞에 오게 함

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")