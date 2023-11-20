# the paint can says that 1 can of paint can cover 5 square meters of wall.
# Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5 = 1.6


# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    amount_of_can = height * width / cover
    ceiled_amount_of_can = math.ceil(amount_of_can)
    print(f"You'll need {ceiled_amount_of_can} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m), input = 4
test_w = int(input()) # Width of wall (m), input = 5
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
