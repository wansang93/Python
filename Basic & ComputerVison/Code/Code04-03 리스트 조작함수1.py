# 특정값의 모든 위치를 출력하는 프로그램
import random
myList = [random.randint(1, 5) for _ in range(10)]
print(myList)

NUMBER = 5

index = 0
findList = []
print('찾을 숫자:', NUMBER, '처음 있는 위치:', myList.index(NUMBER, index))
# myList.index(값, 몇번째)를 사용할 때 주의점
# myList에 값이 없으면 오류를 발생시킨다.

while True:
    try:
        index = myList.index(NUMBER, index)
        findList.append(index)
        index += 1
    except:
        break

print(NUMBER, '가 있는 위치들', findList)
