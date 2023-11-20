"""
문자형 index
ex) a = "23"

a[0] = 2
a[1] = 3

숫자형 index

ex) a = 23

숫자형은 indexing을 할 수 없다.


문자형 slicing

>>> a = "Life is too short, You need Python"
>>> a[0:4]
'Life'

>>> index(letter)
string, list, tuple에서 사용
찾는 문자가 없으면 ValueError 발생
첫번재 찾는 문자의 index를 출력

>>> find(letter)
string에서 사용
찾는 문자가 없으면 -1
str.find("x", 0, 3) -> list에서 0부터 3까지 사이에서 x를 find
첫번재 찾는 문자의 index를 출력
"""