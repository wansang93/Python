# 특정값의 모든 위치를 출력하는 프로그램
import random
myList = [ random.randint(1,5) for _ in range(10)]
print(myList)

NUMBER = 5

index = 0
findList = []


for i in range(myList.count(NUMBER)):
    index = myList.index(NUMBER, index)
    findList.append(index)
    index += 1

print(NUMBER, '가 있는 위치들', findList)
