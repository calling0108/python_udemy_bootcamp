# Input a Python list of student heights

# 기존 문제는 해당 리스트를 input으로 값을 받게 해놓았음. student_heights = input().split()
student_heights = [180, 124, 165, 173, 189, 169, 146] 
for n in range(0, len(student_heights)): 
    # range 함수를 통해 총 범위를 7개로 산정. input으로 입력받을 때를 대비해서 range 함수로 마지막 계산 범위를 지정해줌
    student_heights[n] = int(student_heights[n]) 
    # input으로 입력받은 수기에 str에서 int로 형 변환 시켜주는 것. index 1의 "124"를 int 124로 변경해줌
    # 그 결과 'student_heights' list는 int type으로 변경됨

# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

# Answer

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

# ME

# total_height = 0
# number_of_students = 0

# for n in range(0, student_heights): # 위에서 input함수로 list의 범위가 정해졌기에 len함수를 사용하지 않아도 됨
#     total_height += student_heights[n]
#     number_of_student = n + 1

# average_height = round(total_height / number_of_student)

# print(f"total height = {total_height}")
# print(f"number of students = {number_of_student}")
# print(f"average height = {average_height}")
