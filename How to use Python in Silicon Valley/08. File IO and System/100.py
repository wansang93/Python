import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/empty.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # 압축하기
    # z.extractall('zip_file')
    with z.open('test_dir/empty.txt') as f:
        print(f.read())