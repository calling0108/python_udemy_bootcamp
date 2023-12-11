target = int(input("Type number: ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

if target > 1000 or target < 0:
    print("Please type. number < 1,000")
else:
    total = 0
    for n in range(0, target + 1, 2):
        total += n
    print(total)


# ANSWER (또 다른 답)
alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0: # if 조건에 해당하면 수행하게 하기에 for loop에서 1,3,5... 등의 홀수는 실행하지 않아도 오류가 발생하지 않음.
        alternative_sum += number
print(alternative_sum)