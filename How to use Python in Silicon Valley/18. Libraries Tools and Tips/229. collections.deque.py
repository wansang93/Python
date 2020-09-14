import collections
import queue

# Double-end queue
collections.deque

q = queue.Queue()  # first in first out
lq = queue.LifoQueue()  # last in first out
l = []
d = collections.deque()  # 메모리 관계상 효율적으로 관리함

#
for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# 해당 자료구조에서 하나씩 꺼내기
for _ in range(3):
    print(f'FIFO: {q.get()}')
    print(f'LIFO: {lq.get()}')
    print(f'list: {l.pop()}')
    print(f'd   : {d.pop()}')
    # print(f'list: {l.pop(0)}')  # 제일 앞에 꺼내기
    # print(f'd   : {d.popleft()}')  # 제일 앞에 꺼내기
    print()

for i in range(3):
    d.append(i)

# 회전하기
print(d)  # deque([0, 1, 2])
d.rotate()
print(d)  # deque([2, 0, 1])
d.rotate()
print(d)  # deque([1, 2, 0])

# 삽입하기
d.extend('x')
print(d)  # deque([1, 2, 0, 'x'])
d.extendleft('y')
print(d)  # deque(['y', 1, 2, 0, 'x'])
