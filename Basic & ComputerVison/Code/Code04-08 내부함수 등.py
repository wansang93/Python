# 내부함수
def outFunc(v1, v2):
    def inFunc(n1, n2):
        return n1 + n2
    return inFunc(v1, v2)

print(outFunc(100, 200))

# (1) 함수에서 lambda 표현식으로
def hap (v1, v2):
    res = v1 + v2
    return res

hap2 = lambda v1, v2 : v1+v2

print(hap(100,200))
print(hap2(100,200))

# (2) 함수에서 lambda 표현식으로
def add10(num):
    return num + 10

lambda_add10 = lambda num: num+10

# 리스트에 10을 더하는 방법 3가지
myList = [1, 2, 3, 4, 5]

for i in range(len(myList)):
    myList[i] = add10(myList[i])
print(myList)

myList = list(map(lambda_add10, myList))
print(myList)

myList = list(map(lambda num: num+10, myList))
print(myList)
