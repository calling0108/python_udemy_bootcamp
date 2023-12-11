programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}



print(programming_dictionary["Bug"]) # 같은 type으로 불러와야 함 [Bug] X, ["Bug"]

# Adding new items to dictionary.
# dictionary를 새로 추가해줄 때
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}


# Wipe an existing dictionary
# 존재하는 dictionary의 key와 value를 지워줄 때
# 점수 초기화 등 사용할 때
programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # key 값만 출력됨
    print(programming_dictionary[key]) # value 값 출력
 
    