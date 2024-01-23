print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))

# 총 금액 / 사람 인원 수 * 퍼센트
bill_with_the_tip = total_bill + tip / 100 * total_bill

each_person_pay = round(bill_with_the_tip / people_number, 2)

pay = f"Each person should pay: ${each_person_pay}"

print(pay)