# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 내가 푼거
pay = 0


if size == "S":
    pay = 15
    if add_pepperoni == "Y":
        pay += 2
        if extra_cheese == "Y":
            pay += 1
            print(f"Your final bill is: ${pay}.")
        else:
            print(f"Your final bill is: ${pay}.")
    else:
        pay += 15
        print(f"Your final bill is: ${pay}.")
elif size == "M":
    pay = 20
    if add_pepperoni == "Y":
        pay += 3
        if extra_cheese == "Y":
            pay += 1
            print(f"Your final bill is: ${pay}.")
        else:
            print(f"Your final bill is: ${pay}.")
    else:
        pay += 15
        print(f"Your final bill is: ${pay}.")
elif size == "L":
    pay = 25
    if add_pepperoni == "Y":
        pay += 3
        if extra_cheese == "Y":
            pay += 1
            print(f"Your final bill is: ${pay}.")
        else:
            print(f"Your final bill is: ${pay}.")
    else:
        pay += 15
        print(f"Your final bill is: ${pay}.")
else:
    print("Please choose S, M or L size.")

# anwer 
# 2번째 풀었는데도 또 틀렸다..ㅋㅋ

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y": # else 문이 필요없음. 조건이 필요하면 넣고 필요없으면 아무 조건 값도 없으니까.
    bill += 1

print(f"Your final bill is ${bill}.")


