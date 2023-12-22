#Print is Your Friend

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# '=='은 좌우측의 값이 같다는 것이고, 이때 우측의 값을 250을 입력할 경우 좌측 0, 우측 250이므로 boolean 연산에 의거하여 False값이 출력됨. 이 줄이 거짓이면 코드는 이 줄을 무시하고 진행하기에 값이 '0'이 됨.
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page
print(total_words)