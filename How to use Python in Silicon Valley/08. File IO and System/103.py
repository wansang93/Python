import datetime

now = datetime.datetime.now()
print(now)  # 2020-07-24 18:46:11.346924
print(now.strftime('%d/%m/%y - %H:%M:%S.%f'))

today = datetime.date.today()
print(today)  # 2020-07-24
print(today.isoformat())  # 2020-07-24
print(today.strftime('%d-%m-%y'))  # 24-07-20

t = datetime.time(hour=1, minute=30, second=30, microsecond=30)
print(t)

# timedelta 메서드를 활용하면 시간을 빼고 더할 수 있습니다.
datetime.timedelta(days=365)
datetime.timedelta(hours=3)
d = datetime.timedelta(minutes=5)
print(now - d)  # 5분 전

# 시간 로그가 적힌 백업 파일에 만들기
import os
import shutil

file_name = 'text.txt'

with open(file_name, 'w') as f:
    f.write('test')

if os.path.exists(file_name):
    # text.txt.2020_07_24_23_03_40 파일 생성
    shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))