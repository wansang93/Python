# 파일이나 폴더를 만들고 바로 지움
import tempfile

# 파일 만들기
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 버퍼가 아닌 temp 폴더에 파일 만들기
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        print(f.read())

# temp 폴더에 폴더 만들기
with tempfile.TemporaryDirectory() as td:
    print(td)

# 폴더 지우기 방지
temp_dir = tempfile.mkdtemp()
print(temp_dir)