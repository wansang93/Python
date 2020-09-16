import re

s = 'My name is !@# Mike'
print(s.split())  # ['My', 'name', 'is', '!@#', 'Mike']

p = re.compile(r'\W+')
print(p.split(s))  # ['My', 'name', 'is', 'Mike']

p = re.compile(r'(blue|white|red)')
print(p.sub('colour', 'blue time white red black'))  # colour time colour colour black
print(p.sub('colour', 'blue time white red black', count=1))  # colour time white red black  
print(p.subn('colour', 'blue time white red black'))  # ('colour time colour colour black', 3)


# 특정 문자에 숫자들을 16진수로 바꾸기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrepl, '12345 95 11 test test2'))  # 0x10x20x30x40x5 0x90x5 0x10x1 test test0x2