import re

s = '<html><head><title>Title</title></head></html>'

print(re.findall('<.*>', s))  # 1개 출력
# ['<html><head><title>Title</title></head></html>']
print(re.findall('<.*?>', s))  # 6개 출력
# ['<html>', '<head>', '<title>', '</title>', '</head>', '</html>']