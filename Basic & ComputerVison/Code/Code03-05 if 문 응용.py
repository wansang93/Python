import random

numbers = []

for _ in range(0, 10) : # for (i=0; i<10; i++)
    numbers.append(random.randint(0,9))

print(numbers)

for num in range(0, 10) :
    if num not in numbers :
        print(num, '이 없어요')