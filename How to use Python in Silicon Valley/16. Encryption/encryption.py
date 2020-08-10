import string
import random
import io

from Crypto.Cipher import AES

# 킷값 생성
key = ''.join(
    random.choice(string.ascii_letters) for i in range(AES.block_size)).encode("utf8")

# iv값 생성
iv = ''.join(
    random.choice(string.ascii_letters) for i in range(AES.block_size)).encode("utf8")

# plaintext = 'adsfsadfwwwer3'

# # 암호화
# cipher = AES.new(key, AES.MODE_CBC, iv)
# padding_length = AES.block_size - len(plaintext) % AES.block_size
# plaintext += chr(padding_length) * padding_length
# plaintext = plaintext.encode("utf-8")
# cipher_text = cipher.encrypt(plaintext)
# print(plaintext)

# # 복호화
# cipher2 = AES.new(key, AES.MODE_CBC, iv)
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text[:-decrypted_text[-1]])

# 파일에 응용
file_path = r'C:\Users\wansang\Desktop\Gitrep\Python\How to use Python in Silicon Valley\16. Encryption'

with open(file_path + r'\plaintext.txt', 'r') as f, open(file_path + r'\enc.dat', 'wb') as e:
    # 파일 읽어오기
    plaintext = f.read()

    # 패딩하기
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    plaintext = plaintext.encode("utf-8")
    
    # 암호화
    cipher_text = cipher.encrypt(plaintext)
    print(cipher_text)
    e.write(cipher_text)

with open(file_path + r'\enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = f.read()
    decrypted_text = cipher2.decrypt(ciphertext)
    print(decrypted_text[:-decrypted_text[-1]])