import logging
import contextlib

#4. 에러 메세지를 log에 적어 파일화 하기

# # 참고: logging.error 와 sys.stderr.write
# logging.error('Error!')
# sys.stderr.write('Error!')

# Error logging은 항상 stderr를 쓰게 돼 있지만
# stdout을 통해서 파일에 적을 수 있음
# 특히 contextlib.redirect_stdout을 통해 logging하면 편함

file_path = (r'C:/Users/wansang/Desktop/Gitrep/Python/How '
    r'to use Python in Silicon Valley/18. Libraries Tools and Tips')

with open(file_path + '/stderr.log', 'w') as ff:
    with contextlib.redirect_stderr(ff):
        logging.error('Error!')