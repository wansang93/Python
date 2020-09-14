import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),
     ('red', 1), ('blue', 4)]

c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
print(c.most_common(2))  # 2번째로 많은 값들 return(중복 x)
print(c.values())

import re
import os

with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
    words = re.findall('\\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))

