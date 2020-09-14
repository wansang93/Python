import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),
     ('red', 1), ('blue', 4)]

for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

d2 = {}
for word in l:
    d2.setdefault(word, 0)
    d2[word] += 1
print(d2)

d3 = collections.defaultdict(int)
for word in l:
    d3[word] += 1
print(d3)

d4 = collections.defaultdict(set)
for k, v in s:
    d4[k].add(v)
print(d4)