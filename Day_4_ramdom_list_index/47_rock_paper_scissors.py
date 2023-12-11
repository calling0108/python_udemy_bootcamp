rock = '''
    _______
---'   ____)
      (_____)   
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''  
    _______
---'   ____)____
          ______)
    __________)  
      (____)
---.__(___)
'''     

#Write your code below this line 👇
# rock = 0, paper = 1, scissors = 2


import random

# user와 pc의 0~2 값을 출력
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice = random.randrange(0,3)

paper_list = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0: # 41행 print문의 index에서 0보다 작거나 3보다 큰 수를 입력하면 paper_list의 list내 인덱스 범위를 벗어나게 되기에 조건문을 작성해줌으로 오입력을 방지한다.
    print("You typed an invalid number, you lose!")
else:
    print(paper_list[user_choice]) # user_choice는 int니까, 변수명의 항목이 int type이면 변수명으로 list indexing 가능.

    print(f"pc_choice is {pc_choice}")
    print(paper_list[pc_choice])

    if user_choice == 0 and pc_choice == 2:
        print("You Win!")
    elif user_choice == 2 and pc_choice == 0:
        print("You lose.")
    elif user_choice > pc_choice:
        print("You Win!")
    elif user_choice == pc_choice:
        print("Draw.")

"""
>>> ME

# 0 : rock, 1 : paper, 2 : scissor 출력되게
# if user_choice == 0:
#     print(rock)     
# elif user_choice == 1:
#     print(paper)
# else:           
#     print(scissors)

# if pc_choice == 0:
#     print(f"Computer chose: \n" + rock)
# elif pc_choice == 1:
#     print(f"Computer chose: \n" + paper)
# else:
#     print(f"Computer chose: \n" + scissors)

# 0 < 1
# 0 > 2
# 2 > 1

# rock
# paper
# scissors

"""