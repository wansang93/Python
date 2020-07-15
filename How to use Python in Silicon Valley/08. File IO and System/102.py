import os
import subprocess

# 옛날 방식
os.system('ls')

# 요즘 방식
subprocess.run(['ls', '-al'])

# 쉬운 방식
# 단점: 보안상 안전하지 않다. 명령어에 다 지우기 등을 추가할 수 있다.
print('=' * 10)
subprocess.run('ls -al | grep test', shell=True)

# 리턴 코드를 이용해서 exception 발생 가능, 또는 check 옵션으로 가능
r = subprocess.run('ls', shell=True, check=True)
print(r)

# 파이프를 써서 shell injection attack 을 피하는 방법
print('=' * 10, 'defense shell injection')
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
