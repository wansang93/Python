import enum

class Status(enum.Enum):
    ACTIVE = 1
    # ACTIVE = 2 -> error occured
    RENAME_ACTIVE = 1  # no error, 다른 name으로 1의 name을 불러올 때
    INACTIVE = 2
    RUNNING = 3

print(Status.ACTIVE)  # Status.ACTIVE
print(repr(Status.ACTIVE))  # <Status.ACTIVE: 1>
print(Status.ACTIVE.name)  # ACTIVE
print(Status.ACTIVE.value)  # 1

for s in Status:
    print(s)
    print(type(s))

print(Status(1))  # Status.ACTIVE

print(Status.RENAME_ACTIVE)

# 데이터 베이스 경우 아래 경우는 느림, 문자열이 value 이기 때문에
db = {
    'stack1': 'active',
    'stack2': 'inactive',
}

if db['stack1'] == 'active':
    print('shutdown111')
elif db['stack2'] == 'inactive':
    print('terminate')

# 개선
db = {
    'stack1': 1,
    'stack2': 2,
}

STATUS_ACTIVE = 1
STATUS_INACTIVE = 2

if db['stack1'] == 1:
    print('shutdown222')
elif db['stack2'] == 2:
    print('terminate')

# 더 개선
class Status2(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

if Status2(db['stack1']) == Status2.ACTIVE:
    print('shutdown333')
elif Status2(db['stack1']) == Status2.INACTIVE:
    print('terminate')

###
# @enum.unique  # value의 unique 하지 않으면 error occur
class Status3(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

if db['stack1'] == Status3.ACTIVE:
    print('shutdown444')
elif db['stack1'] == Status3.INACTIVE:
    print('terminate')

print(Status3.ACTIVE)
print(type(Status3.ACTIVE))
print(Status3.ACTIVE == 1)
# Status3.ACTIVE
# <enum 'Status3'>
# True

###
class Perm(enum.IntFlag):
    R = 4  # READ
    W = 2  # WRITE
    X = 1  # 엑스큐션(?)

print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W | Perm.X))
RWX = Perm.R | Perm.W | Perm.X
print(Perm.W in RWX) 
# Perm.R|W
# <Perm.R|W|X: 7>
# True