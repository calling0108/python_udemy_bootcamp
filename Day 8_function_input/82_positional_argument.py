# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")


# greet_with("somyoung", "seoul")


# Positional Arguments, 위치값 존재
greet_with("Seoul", "somyoung") # Hello Seoul, what is it like in somyoung

def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    print(a, b, c)

my_function(1, 2, 3) # a = 1, b = 2, c = 3


# Keyword Arguments
def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    print(a, b, c)

my_function(c = 3, a = 1, b = 2) # a = 1, b = 2, c = 3

def greet_with_2(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_2(location = "Daegu", name = "hyunju")

