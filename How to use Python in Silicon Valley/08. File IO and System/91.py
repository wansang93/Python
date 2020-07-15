file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.txt')

f = open(file_path, 'w')
f.write('wansang\n')
f.write('한글\n')
print('한글 I want to write Korean!', file=f)
f.close()