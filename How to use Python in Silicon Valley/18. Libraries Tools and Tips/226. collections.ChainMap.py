# 복잡한 딕셔너리를 다룰때는 ChainMap을 쓰면 좋아요
import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# print(a)  # {'a': 'a', 'c': 'c', 'num': 0}
# a.update(b)  # 중복된 값은 덮어 쓰기
# print(a)  # {'a': 'a', 'c': 'cc', 'num': 0, 'b': 'b'}

# 덮어 쓰기 되돌리기가 불가해서 체인 맵 사용해서 해결
m = collections.ChainMap(a, b, c)
print(m)
print(m.maps)  # m을 리스트로 반환
print(m['c'])  # 순서 상 제일 앞쪽에서 부터 사용
# ChainMap({'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'})
# [{'a': 'a', 'c': 'c', 'num': 0}, {'b': 'b', 'c': 'cc'}, {'b': 'bbb', 'c': 'ccc'}]
# c

m.maps.reverse()  # m을 거꾸로 하여
print(m.maps)  # m을 리스트로 반환
print(m['c'])  # 기존 m의 뒤에서(m의 reverse)부터 c값을 찾음
# [{'b': 'bbb', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]
# ccc

m.maps.insert(0, {'c': 'CCCCCC'})  # create: m의 0번째에 key값에 c, value값에 CCCCCC를 넣음
print(m.maps)  # read
print(m['c'])
# [{'c': 'CCCCCC'}, {'b': 'bbb', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]
# CCCCCC

del m.maps[0]  # delete

m['b'] = 'BBBBB'  # update
print(m.maps)
# [{'b': 'BBBBB', 'c': 'ccc'}, {'b': 'b', 'c': 'cc'}, {'a': 'a', 'c': 'c', 'num': 0}]

# ChainMap을 상속받아서 원하는 기능을 더 넣을 수 있어요
class DeepChainMap(collections.ChainMap):
    # setitem은 딕셔너리에서 세팅을 할 때 기본적으로 나오는 함수에요
    def __setitem__(self, key, value):
        # ChainMap을 순회
        for mapping in self.maps:
            # value의 type이 int 이고 그 값이 넣으려는 값보다 작으면
            if type(mapping[key]) is int and mapping[key] < value:
                # 갱신
                mapping[key] = value
            return
        # 위에 해당사항이 없으면 0번째에 생성
        self.maps[0][key] = value

m = DeepChainMap(a, b, c)
print(m)
# DeepChainMap({'a': 'a', 'c': 'c', 'num': 1}, {'b': 'b', 'c': 'cc'}, {'b': 'BBBBB', 'c': 'ccc'})

m['num'] = 1
print(m['num'])  # 1
m['num'] = -1
print(m['num'])  # 1
