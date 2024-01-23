def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not leap year"
        else:
            return "Leap year"
    else:
        return "Not leap year"
  
# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29] 
    answer = is_leap(year)
    if answer == "Leap year" and month == 2:
        return month_days[12]
    else:
        one_days = month_days[month - 1]
        return one_days
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

# Answer
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29] 
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)