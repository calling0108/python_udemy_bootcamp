# Randomisation 무작위화

import random # random 모듈은 python 모듈
import my_module

random_integer = random.randint(1, 10) # 1~10 사이의 정수 난수(random number) 출력

random_float = random.random() # 0과 1 사이의 부동 소수점 난수 출력
print(random_float * 5)

print(my_module.pi)