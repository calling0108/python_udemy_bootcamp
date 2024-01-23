# Input a list of student scores

# student_scores = input().split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

# 답안

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# ME

# highest_score = 0

# for n in range(0, student_scores):
#     if highest_score < student_scores[n]:
#         highest_score = student_scores[n]

# print(f"The highest score in the class is: {highest_score}")

