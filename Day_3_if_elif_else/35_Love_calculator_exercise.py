# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

true = t + r + u + e
love = l + o + v + e

answer = str(true) + str(love)
int_answer = int(answer)

# answer = int(str(true) + str(love)) 방법도 가능

if int_answer < 10 or (int_answer > 90): # python에서는 조건들을 ()로 싸줘도 좋다. ex) (int_answer < 10) or (int_anwer > 90):
    print(f"Your score is {answer}, you go together like coke and mentos.")
elif 40 <= int_answer <= 50:
    print(f"Your score is {answer}, you are alright together.")
else:
    print(f"Your score is {answer}.")
