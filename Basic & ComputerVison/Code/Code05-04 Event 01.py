from tkinter import messagebox
import tkinter
def click_left(event):
    txt = ''
    if event.num == 1:
        txt += '왼쪽 버튼: '
    elif event.num == 2:
        txt += '가운데 버튼: '
    elif event.num == 3:
        txt += '오른쪽 버튼: '
    
    txt += str(event.x) + ',' + str(event.y)
    messagebox.showinfo('제목', txt)


def key_press(event):
    messagebox.showinfo('제목', chr(event.keycode))


# main code
if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry('400x400')

    photo = tkinter.PhotoImage(file='C:/images/Pet_GIF/Pet_GIF(256x256)/cat01_256.gif')

    label1 = tkinter.Label(window, image=photo)
    label1.bind('<Button>', click_left)

    window.bind('<Key>', key_press)
    label1.pack(expand=1, anchor=tkinter.CENTER)

    window.mainloop()
