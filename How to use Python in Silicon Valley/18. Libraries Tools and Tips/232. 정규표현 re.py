import re

'''
match()     문자열 처음부터 정규식과 매치되는지 조사
search()    문자열 전체를 검색하여 정규식과 매치되는지 조사
findall()   정규식과 매치되는 모든 문자열을 리스트로 리턴
finditer()  정규식과 매치되는 모든 문자열을 iterator 객체로 리턴
'''

m = re.match('a.c', 'abc')
print(m)  # <re.Match object; span=(0, 3), match='abc'>
print(m.group())  # abc

m = re.search('a.c', 'abc')
print(m)  # <re.Match object; span=(0, 3), match='abc'>
print(m.span())  # (0, 3)
print(m.group())  # abc

m = re.finditer('a.c', 'test abc test abc')
print(m)  # # <callable_iterator object at 0x000001B484E49550>
print([w.group() for w in m])  # ['abc', 'abc']

# . -> 아무거나
# ? -> 1개
# + -> 1번 이상
# * -> 0번 이상
# {2, 4} -> 2개 이상 4개 이하
# ^ -> not
# ^ -> 제일 앞에 올때는 시작하는 부분이 맞는지
# $ -> 제일 뒤에 쓰고 끝나는 부분이 맞는지

# re documents
# https://docs.python.org/3.8/library/re.html?highlight=re#module-re