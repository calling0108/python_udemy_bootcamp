fruits = ["Cherry", "Apple", "Pear"]

# List는 data의 순서가 있어서 Indexing 할 수 있음.

fruits[1]   # Apple
fruits[-1]  # Pear, -0은 불가능한 값이다.

fruits[1] = "Banana"    # 항목 변경


fruits.append("Grape")   # 마지막에 Grape 추가
fruits.extend(["Strawberry", "Blueberry"]) # 여러 개의 항목을 list의 마지막에 추가


# https://docs.python.org/3/tutorial/datastructures.html