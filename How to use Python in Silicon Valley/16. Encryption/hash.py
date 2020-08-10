import base64
import os
import hashlib

print(hashlib.sha256(b'password').hexdigest())
print(hashlib.sha256(b'password').hexdigest())

user_name = 'wansang93'
user_pass = 'password'

db = {}

salt = base64.b64encode(os.urandom(32))
print(salt)

# digest 만들기(암호화 작업)
def get_digest(password):
    password = bytes(user_pass, 'utf-8')
    print(password)
    # salt 기법
    digest = hashlib.sha256(salt + password).hexdigest()
    # stretch 기법
    for _ in range(10000):
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
    return digest

db[user_name] = get_digest(user_pass)

print(db)

def is_login(user_name, password):
    return get_digest(password) == db[user_name]

print(is_login(user_name, user_pass))


# 위에 함수를 한번에 하기
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000)

db[user_name] = digest

def is_login2(user_name, password):
    digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000)
    return digest == db[user_name]

print(is_login2(user_name, user_pass))