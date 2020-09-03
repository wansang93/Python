import io

file_path = ('C:/Users/wansang/Desktop/Gitrep/Python' +
    '/How to use Python in Silicon Valley/18. Libraries Tools and Tips')

with open(file_path + '/a.txt', 'w') as f:
    f.write('test test')

with open(file_path + '/a.txt', 'r') as f:
    print(f.read())

# f = io.StringIO()
# f.write('string io test')
f = io.BytesIO()
f.write(b'byte io test')
f.seek(0)
print(f.read())

# 파일을 다운받지 않고(디스크에 쓰지 않고) 파일을 조작하고 열 수 있음
# 예를 들어 디스크에 안쓰고 메모리에 쓰고 바로 지울 수 있음

import io
import requests
import zipfile

url = ('https://files.pythonhosted.org/packages/fd/53/'
       'a626e098cbbc443a5bba1e0f780d1fe97115218a8f5d1e2df6bfa1f47a31/'
       'setuptools-50.1.0.zip')

r = requests.get(url)
f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-50.1.0/README.rst') as r:
        print(r.read().decode())
