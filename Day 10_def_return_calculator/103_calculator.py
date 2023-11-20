from art import logo
from replit import clear

print(logo)

def operations(number_1st, number_2nd, operator):
    global answer
    answer = 0
    if operator == "+":
        answer = number_1st + number_2nd
        return answer
    elif operator == "-":
        answer = number_1st - number_2nd
        return answer
    elif operator == "*":
        answer = number_1st * number_2nd
        return answer
    elif operator == "/":
        answer = number_1st / number_2nd
        return answer
    else:
        print("Please type like this -> +-*/ ")

should_continue = False

while not should_continue:
    first_number = float(input("What's the first number: "))
    print("+\n" + "-\n" + "*\n" + "/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))

    
    #  input 값인 operation과 함수명을 동일하게 해서 'str' 오류가 발생함.. 3일 걸렸다..
    operations(number_1st = first_number, number_2nd = second_number, operator = operation)
    
    print(f"{first_number} {operation} {second_number} = {answer}")

    retry = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    if retry == "n":
        should_continue = True
    elif retry == "y":
        clear()
    else:
        print("Please type 'y' or 'n'. ")


# Answer

# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide
# }

# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Pick an opeartion from the line obove: ")
# num2 = int(input("What's the second number?: "))

# calculation_function = operations[operation_symbol]

# answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {answer}")
