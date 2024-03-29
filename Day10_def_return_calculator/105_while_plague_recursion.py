from art import logo
from replit import clear

print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = False
    while not should_continue:
        operation_symbol = input("Pick an opeartion: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        retry = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' is end of calculating: ")

        if retry == "n":
            should_continue = True
            clear()
            calculator()
        elif retry == "y":
            num1 = answer
        elif retry == "exit":
            should_continue = True
        else:
            print("Please type 'y' or 'n'. ")

calculator()