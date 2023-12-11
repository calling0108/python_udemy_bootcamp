names_string = "Angela, Ben, Jenny, Michael, Cloe"

names = names_string.split(", ") 
# split() 함수는 문자열을 이쁘게 나눠서 리스트화 함
# names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Cloe']

# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

num_items = len(names) # 5

# 5개 이름 속에서 1명의 이름을 도출해내야 한다
random_choice = random.randint(0, num_items - 1 ) # int type

# 랜덤으로 도출된 숫자를 통해 names 목록
pay_person = names[random_choice]

print(f"{pay_person} is going to buy the meal today!")


"""
📌 내장함수와 메소드는 차이가 있다.

ex)

내장함수 : len(string)
메소드 : object.upper()

메소드는 object(객체) 뒤 '.(콤마)'를 붙이고 사용한다


'class and its Object'의 개념.
함수는 독립적으로 정의되므로 이름으로만 호출이 가능함.
그러나 메소드는 이름으로만 호출되지 않음. 정의된 클래스의 참조에 의해 클래스를 호출해야한다.
메소드는 클래스 내에서 정의되므로 해당 클래스에 종속된다.

함수가 메소드보다 더 포괄적인 의미를 가진다.

https://velog.io/@yejin20/Python-%ED%95%A8%EC%88%98%EC%99%80-%EB%A9%94%EC%86%8C%EB%93%9C%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90

"""