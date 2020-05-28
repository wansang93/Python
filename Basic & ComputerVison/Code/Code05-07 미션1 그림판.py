import tkinter
import tkinter.simpledialog
import tkinter.colorchooser

# 전역 변수 부분
window = None
canvas = None
x1, x2, y1, y2 = None, None, None, None
pen_color = 'black'
pen_width = 5
shape = 'Line'


# 함수 부분
def mouse_click(event):
    global x1, x2, y1, y2
    x1 = event.x
    y1 = event.y

def mouse_drop(event):
    global x1, x2, y1, y2, pen_color, pen_width
    x2 = event.x
    y2 = event.y
    if shape == 'Line':
        canvas.create_line(x1, y1, x2, y2, width=pen_width, fill=pen_color)
    elif shape == 'Oval':
        canvas.create_oval(x1, y1, x2, y2, width=pen_width, fill='white', outline=pen_color)

def get_color():
    global pen_color
    color = tkinter.colorchooser.askcolor()
    pen_color = color[1]

def get_width():
    global pen_width
    pen_width = tkinter.simpledialog.askinteger(
        '선 두께', '선 두께(1~30)를 입력하세요', minvalue=1, maxvalue=30)

def get_line_shape():
    global shape
    shape = 'Line'

def get_oval_shape():
    global shape
    shape = 'Oval'


# 메인 코드
if __name__ == "__main__":

    window = tkinter.Tk()
    window.title('그림판 ver0.01')
    window.geometry('400x400')
    canvas = tkinter.Canvas(window, height=300, width=300, background='white')
    canvas.bind('<Button-1>', mouse_click)
    canvas.bind('<ButtonRelease-1>', mouse_drop)
    canvas.pack()

    main_menu = tkinter.Menu(window)
    window.config(menu=main_menu)
    
    file_menu = tkinter.Menu(main_menu)
    main_menu.add_cascade(label='설정', menu=file_menu)
    shape_menu = tkinter.Menu(main_menu)
    main_menu.add_cascade(label='도형', menu=shape_menu)

    file_menu.add_cascade(label='선 색상 선택', command=get_color)
    file_menu.add_separator()
    file_menu.add_command(label='선 두께 설정', command=get_width)

    shape_menu.add_cascade(label='선', command=get_line_shape)
    shape_menu.add_cascade(label='원', command=get_oval_shape)

    window.mainloop()
