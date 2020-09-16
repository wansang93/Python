# repr  # representation
print(1)  # 1
print(str(1))  # 1
print(repr(1))  # 1
print(repr(str(1)))  # '1'

# 
import datetime
d = datetime.datetime.now()
print(d)  # 2020-09-16 23:00:27.783250
print(str(d))  # 2020-09-16 23:00:27.783250
print(repr(d))  # datetime.datetime(2020, 9, 16, 23, 0, 27, 783250)

# representation 표시법
test = 'test'
test1 = 'test1'
test2 = 'test2'
print(f'{test!r} {test1} {test2!s}')

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return f'Point({self.x}, {self.y})'

p = Point(10, 20)
print(f'{p!r} {p} {p!s}')
# Point<object> Point(10, 20) Point(10, 20)
