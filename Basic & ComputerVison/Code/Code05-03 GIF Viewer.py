import tkinter as tk
from tkinter import messagebox

# 전역 변수 선언부
dir_name = 'C:/images/Pet_GIF/Pet_GIF(256x256)/'
files_name = [
    'cat01_256.gif',
    'cat02_256.gif',
    'cat03_256.gif',
    'cat04_256.gif',
    'cat05_256.gif',
    'cat06_256.gif',
]

# 함수 선언부
def open_file():
    pass


# 메인 코드
if __name__ == "__main__":
    window = tk.Tk()
    window.title('GIF 사진 뷰어 Beta(Version 0.01)')
    window.geometry('400x400')
    window.resizable(width=True, height=True)

    photo = tk.PhotoImage(file=dir_name + files_name[0])
    label1 = tk.Label(window, image=photo, anchor=tk.CENTER)

    button = tk.Button(window, text='종료', command=open_file)

    
    label1.pack()
    button.pack()

    window.mainloop()
