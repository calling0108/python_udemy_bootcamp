# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2), 2)

print(bmi)

if bmi > 35:
    print("They are clinically obese.")
elif bmi > 30:
    print("They are obese.")
elif bmi > 25:
    print("They are overweight.")
elif bmi > 18.5:
    print("They have a normal weight.")
else:
    print("They are underweight.")
