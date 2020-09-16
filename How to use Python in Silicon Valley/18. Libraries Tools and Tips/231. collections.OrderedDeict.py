import collections

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Python 2.7.9 이전 버전은 dictionary가 순서가 보장이 안됨
od = collections.OrderedDict(d)
print(od == d)

print(sorted(od.items(), key=lambda x: x[0]))
print(sorted(od.items(), key=lambda x: x[1]))
print(sorted(od.items(), key=lambda x: len(x[0]), reverse=True))