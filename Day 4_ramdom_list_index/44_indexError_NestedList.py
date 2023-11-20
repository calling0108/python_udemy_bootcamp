# Index out of range error

# Index 범위 밖에 있는 숫자를 출력할 때 IndexError 발생. 
# 대규모 데이터를 다룰 때 주로 발생
# 주로 1개의 숫자 오차로 발생하여 Off-by-one 오류라고 함.


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

nums_of_states = len(states_of_america) # nums_of_States = 50

print(states_of_america[nums_of_states - 1]) # num_of_states = 50인 상황이기에 바로 출력하면 index out of range error가 발생.



# 과일 / 채소 가운데 기생충 이 많은 순위
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"] 

# 과일과 채소로 구분하려면?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# 중첩 list
dirty_dozen = [fruits, vegetables]

print(dirty_dozen) 
# dirty_dozen =  [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]