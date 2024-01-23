# Q1. starting_dictionary를 final_dictionary로 변경하는 코드는 무엇일까요?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

# Q2
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
 
print(dict["a"]) # 1
print([dict][0]) # {'a': 1, 'b': 2, 'c': 3}

for key in dict:
    dict[key] += 1 # key 값에 해당하는 value 값만 1을 더해줌
    print(dict)

"""
Answer
{'a': 2, 'b': 2, 'c': 3}
{'a': 2, 'b': 3, 'c': 3}
{'a': 2, 'b': 3, 'c': 4}

"""

# Q3, "Steak"를 출력하는 코드는 무엇일까?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2]) # ['Steak']
print(order["main"][2][0]) # Steak