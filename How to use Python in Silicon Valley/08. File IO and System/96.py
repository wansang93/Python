import string

file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.txt')

s = """\
Hi $name.

$contents

Have a good day
"""

with open(file_path, 'w+') as f:
    f.write(s)
    f.seek(0)
    t = string.Template(f.read())

contents = t.substitute(name='Wansang', contents='How are you?')
print(contents)