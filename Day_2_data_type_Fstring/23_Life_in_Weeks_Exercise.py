# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# maybe we will live until 90 years old.
"""
1 year = 365 days
1 year = 52 weeks
1 year = 12 months
"""

user_days = int(age) * 365
user_weeks = int(age) * 52
user_months = int(age) * 12

left_days = 90 * 365
left_weeks = 90 * 52
left_months = 90 * 12

days = left_days - user_days
weeks = left_weeks - user_weeks
months = left_months - user_months

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


"""

answer

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaning = years_remaining * 52
months_remaining = years_remaning * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
"""