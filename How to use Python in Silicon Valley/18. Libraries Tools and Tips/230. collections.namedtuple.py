import collections

# 1. 일반적인 튜플
p = (10, 20)
print(p[0])  # 10
# p[0] = 100  # -> error 발생

# 2. Point라는 객체로 생성하여 x, y 를 접근하는 방법
# (튜플과 공통점) x값만 외부에서 접근하지 못하게 설정
# (튜플과 차이점) 인덱스가 아닌 이름으로(x, y) 호출 가능
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.y = y

    @property
    def get_x(self):
        return self.__x

p = Point(x=10, y=20)
print(p.get_x)  # 10
# print(p.x)  # -> error 발생: 프라이빗으로 설정하여 접근 불가

# 3. namedtuple: 위에 Point 객체의 장점을 따와 쉽게 만듬
Point2 = collections.namedtuple('Point2_name', ['x', 'y'])
Point3 = collections.namedtuple('Point3_name', 'x, y')
Point4 = collections.namedtuple('Point4_name', 'x y')
p = Point2(10, y=20)
print(p.x)  # 10
# p.x = 100  # error 발생: 튜플이라서

p1 = Point2._make([100, 200])
print(p1)  # Point2_name(x=100, y=200)
print(p1._asdict())  # {'x': 100, 'y': 200}

p1._replace(x=500)  # p1 이 바뀌지 않음
print(p1)  # Point2_name(x=100, y=200)

p2 = p1._replace(x=500)  # p2 만 바뀜
print(p2)  # Point2_name(x=500, y=200)

# 상속 받아 활용하기
class Sumpoint(collections.namedtuple('Point', ['x', 'y'])):
    
    @property
    def total(self):
        return self.x + self.y

p3 = Sumpoint(2, 3)
print(p3.x, p3.y, p3.total)  # 2 3 5

# csv 파일을 namedtuple로 읽어오기
import csv
import os

file_path = os.path.dirname(os.path.abspath(__file__)) + '\\names.csv'

# csv 파일 쓰기
with open(file_path, 'w', newline='\n') as csvfile:
    field_names = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
    writer.writerow({'first': 'Jun', 'last': 'Sakai', 'address': 'B'})
    writer.writerow({'first': 'Nancy', 'last': 'Mask', 'address': 'C'})

# csv 파일 읽어오기
with open(file_path, 'r') as f:
    csv_reader = csv.reader(f)
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.first, names.last, names.address)