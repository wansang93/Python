#  05일차 파이썬 기본문법 160611

## 파이썬

### 책 : 파이썬 for Beginner

#### 10장 - 윈도 프로그래밍

#### 11장 - 파일 입출력

```python
import os
for dirName, subDirList, fnames in os.walk("C:/images/"):
    for fname in fnames:
        if os.path.splitext(fname)[1].upper() == ".GIF":  # splitext .앞을 나눔
            print(os.path.join(dirName, fname))
```

파일은 text file(Ascii)과 Binary로 나눠진다. text파일은 1byte 씩 끊어서 읽는다.

Binary 파일은 각 회사의 노하우가 들어서 byte단위를 끊는 방식이 재각각이다.

```python
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *
import os

# 함수 선언부
def changePhoto():
    global num
    if num > len(fnameList)-1:
        num = 0
    elif num < 0:
        num = len(fnameList)-1
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.photo = photo
    btnName.configure(text=fnameList[num])


def clickNext():
    global num
    num += 1
    changePhoto()


def clickPrev():
    global num
    num -= 1
    changePhoto()


def clickKey(event):
    if event.keycode == 39:  # -> 화살표
        global num
        num += 1
        changePhoto()
    elif event.keycode == 37:  # <- 화살표
        num -= 1
        changePhoto()
    elif event.keycode == 36:  # Home
        num = 0
        changePhoto()
    elif event.keycode == 35:  # End
        num = len(fnameList)-1
        changePhoto()
    elif 49 <= event.keycode and event.keycode <= 54:  # 49는 1, 54는 6
        num = event.keycode-49
        changePhoto()
    else:
        messagebox.showinfo("None", chr(event.keycode))


def clickJump(x):
    global num
    num = (num+x) % len(fnameList)
    changePhoto()


def hopImage(count=0):
    if count == 0:
        count = askinteger("건너뛸 수", "숫자->", minvalue=0, maxvalue=len(fnameList)-1)
    for _ in range(count):
        clickNext()


def selectFile():
    filename = askopenfilename(parent=window,
                               filetypes=(("GIF파일", "*.gif;*.raw"), ("모든파일", "*.*")))
    pLabel.configure(text=str(filename))


# 전역변수 선언부
# dirName = "C:/images/Pet_GIF/Pet_GIF(256x256)/"
# fnameList = ["cat01_256.gif", "cat02_256.gif", "cat03_256.gif",
#              "cat04_256.gif", "cat05_256.gif", "cat06_256.gif"]

fnameList = []
for dirName, subDirList, fnames in os.walk('c:/images/'):
    for fname in fnames:
        if os.path.splitext(fname)[1].upper() == '.GIF':
            fullName = os.path.join(dirName, fname)
            fnameList.append(fullName)

photoList = [None] * 6
num = 0  # 현재 사진 부분

# 메인 코드부
if __name__ == '__main__':
    window = Tk()

    # windows 창 설정
    window.title("GIF 사진(Ver 0.01)")
    window.geometry("700x700")
    window.resizable(width=True, height=True)
    # 메인 메뉴 만들기
    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    filemanu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=filemanu)
    filemanu.add_command(label="열기", command=None)
    filemove = Menu(mainMenu)
    mainMenu.add_cascade(label="이동", menu=filemove)
    filemove.add_command(label="앞으로", command=clickNext)
    filemove.add_separator()
    filemove.add_command(label="뒤로", command=clickPrev)
    filejump = Menu(mainMenu)
    mainMenu.add_cascade(label="n 칸 건더뛰기", menu=filejump)
    # 참고
    # for i in range(len(fnameList)-1):
    # filejump.add_command(label=i+1, command=lambda: clickJump(i+1))
    filejump.add_command(label="1", command=lambda: clickJump(1))
    filejump.add_command(label="3", command=lambda: clickJump(3))
    filejump.add_command(label="5", command=lambda: clickJump(5))
    filejump.add_separator()
    filejump.add_command(label="z", command=selectFile)
    # photo 불러오기
    print(fnameList[num])
    photo = PhotoImage(file=fnameList[num])
    pLabel = Label(window, image=photo)
    # 버튼 설정
    btnPrev = Button(window, text="<< 이전 그림", command=clickPrev)
    btnNext = Button(window, text="다음 그림 >>", command=clickNext)
    btnName = Button(window, text=fnameList[num], command=hopImage)
    # 버튼, 사진 위치 설정
    btnPrev.place(x=10, y=10)
    btnName.place(x=210, y=10)
    btnNext.place(x=510, y=10)
    pLabel.place(x=15, y=50)

    # 키를 눌렀을 때 함수 호출
    window.bind("<Key>", clickKey)

    window.mainloop()
```



``` python
# 한 폴더 안에 모든 GIF파일만 불러오기
import os

for dirName, subDirList, fnames in os.walk("C:/images/"):
    for fname in fnames:
        if os.path.splitext(fname)[1].upper() == ".GIF":
            print(os.path.join(dirName, fname))


# 1. 파일 열기
inFp = open('c:/windows/win.ini', 'rt')  # read text
outFp = open('c:/images/new_win.ini', 'w')  # write

# 2. 파일 읽기/쓰기
# 대용량일 경우 조금씩 읽어야 함
while True:
    inStr = inFp.readline()
    if not inStr:
        break
    outFp.writelines(inStr)
    # print(inStr, end="")

# 소용량일 경우 한번에 읽어도 됨
inStrList = inFp.readlines()
print(inStrList)
for line in inStrList:
    print(line, end="")

# 3. 파일 닫기
inFp.close()
outFp.close()
print("ok")
```

