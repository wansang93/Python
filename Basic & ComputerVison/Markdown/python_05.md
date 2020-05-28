#  05일차 파이썬 기본문법 160611

## 파이썬

### 강의

파일은 text file(Ascii)과 Binary로 나눠진다. text파일은 1byte 씩 끊어서 읽는다.

Binary 파일은 각 회사의 노하우가 들어서 byte단위를 끊는 방식이 재각각이다.

이미지 확장자
  - `bmp`: 하나하나 표현한 파일로 용량이 크다 -> 웹에서는 jpg, jpeg로 대체했다.
  - `jpg`, `jpeg`: 손실 압축된 파일(버리면서 압축한 파일, 복귀 x)
  - `png`: jpg를 만든 회사에서 저작권료를 받으려 해서 나온 파일 확장자
    
    결국 jpg는 저작권료를 받지 않게 바꿨다.

  - `Tiff`, `Tif`: 손실없는 압축파일, 영상처리에서 가장 많이 쓴다.

`콜백함수`는 이벤트가 발생했을 때 실행하게 설정한 함수이다.

#### 폴더 하위 내용 전부 출력하기

``` python
import os

for dir_name, sub_dir_list, f_names in os.walk('C:/images/'):
    for f_name in f_names:
        print(os.path.join(dir_name, f_name))
```

#### 파일명 또는 확장자명 얻기

``` python
import os

os.path.split(f_name)  # 파일명
os.path.splitext(f_name)[1]  # 확장자명
```


### 책 : 파이썬 for Beginner

#### 10장 - 윈도 프로그래밍

여러 기능은 코드 참고

1. 기본 위젯 활용

    * 기본 윈도창의 구성
        ```python
        import tkinter as tk
        window = tk.Tk()
        window.geometry('500x500')
        window.resizable(width=True, height=False)

        window.mainloop()
        ```

#### 11장 - 파일 입출력

코드 참고

### 코드

- 05-01 Sort

    ``` python
    import random

    data_list = [random.randint(1, 99) for _ in range(20)]  # 1부터 99까지
    print(data_list)

    # # Selection Sort
    # for i in range(0, len(data_list)-1):
    #     for j in range(i+1, len(data_list)):
    #         if data_list[i] > data_list[j]:
    #             data_list[i], data_list[j] = data_list[j], data_list[i]

    # Bubble Sort
    for i in range(len(data_list)-1):
        change = False
        for j in range(len(data_list)-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                change = True
        if change == False:
            break

    print(data_list)
    ```

- 05-02 GUI 02

    ``` python
    import tkinter as tk
    import tkinter.messagebox
    '''
    messagebox, along with some other modules like filedialog,
    does not automatically get imported when you import tkinter.
    Import it explicitly, using as and/or from as desired.
    '''

    def click_button():
        tk.messagebox.showinfo('title', 'context')

    def show_image():
        pass

    window = tk.Tk()

    label1 = tk.Label(window, text='Python')
    label2 = tk.Label(window, text='Python', font=('궁서체', 10), bg='skyblue')
    label3 = tk.Label(window, text='Python', bg='blue', width=9, height=2, anchor=tk.CENTER)

    photo = tk.PhotoImage(file='C:/images/Pet_GIF/Pet_GIF(128x128)/cat02_128.gif')
    label4 = tk.Label(window, image=photo)

    button1 = tk.Button(window, text='click me', width=10, height=2, command=click_button)
    button2 = tk.Button(window, text='show image', width=10, height=2, command=show_image)

    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    button1.pack(side=tk.RIGHT)
    button2.pack(side=tk.LEFT)

    window.mainloop()
    ```

- 05-03 GIF Viewer

    ``` python
    import tkinter as tk

    # global variable
    NUM = 0
    dir_name = 'C:/images/Pet_GIF/Pet_GIF(256x256)/'
    f_name_list = ['cat01_256.gif',
        'cat02_256.gif',
        'cat03_256.gif',
        'cat04_256.gif',
        'cat05_256.gif',
        'cat06_256.gif']

    # function


    # main
    if __name__ == "__main__":
        
        window = tk.Tk()
        window.title('GIF Viewer Beta (Ver 0.01)')
        window.geometry('300x300')
        window.resizable(width=True, height=True)

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label = tk.Label(image=photo)

        p_label.place(x=15, y=15)

        window.mainloop()
    ```

- 05-04 Event 01

    ``` python
    from tkinter import messagebox
    import tkinter
    def click_left(event):
        txt = ''
        if event.num == 1:
            txt += '왼쪽 버튼: '
        elif event.num == 2:
            txt += '가운데 버튼: '
        else:
            txt += '오른쪽 버튼: '
        
        txt += str(event.x) + ',' + str(event.y)
        messagebox.showinfo('제목', txt)


    def key_press(event):
        messagebox.showinfo('제목', chr(event.keycode))


    if __name__ == "__main__":
        window = tkinter.Tk()
        window.geometry('400x400')

        photo = tkinter.PhotoImage(file='C:/images/Pet_GIF/Pet_GIF(256x256)/cat01_256.gif')

        label1 = tkinter.Label(window, image=photo)
        label1.bind('<Button>', click_left)

        window.bind('<Key>', key_press)
        label1.pack(expand=1, anchor=tkinter.CENTER)

        window.mainloop()
    ```
- 05-05 파일목록

    ``` python
    import os

    file_address = 'C:/images/'

    # 해당 폴더에서 원하는 확장자만 불러오기
    for dir_name, sub_dir_list, file_names in os.walk(file_address):
        for file_name in file_names:
            if os.path.splitext(file_name)[1].upper() == '.GIF' :
                print(os.path.join(dir_name,file_name))
        # C:/images/Pet_GIF\Pet_GIF(128x128)\cat01_128.gif      
        # C:/images/Pet_GIF\Pet_GIF(128x128)\cat02_128.gif      
        # C:/images/Pet_GIF\Pet_GIF(128x128)\cat03_128.gif      
        # C:/images/Pet_GIF\Pet_GIF(128x128)\cat04_128.gif
        # ...

    for dir_name, sub_dir_list, file_names in os.walk(file_address):
        print(dir_name)
        # 파일 내부에 모든 폴더 주소를 보여줌
        # C:/images/
        # C:/images/csv
        # C:/images/CSV&XLS
        # C:/images/image(BigSize)
        # C:/images/image(BigSize)\image(BigSize)   
        # ...

    for dir_name, sub_dir_list, file_names in os.walk(file_address):
        print(sub_dir_list)
        # 폴더 내부의 폴더들의 주소들을 리스트로 반환, 폴더 내부의 폴더가 존재하지 않을경우 빈 리스트([])로 반환
        # ['csv', 'CSV&XLS', 'image(BigSize)', 'images(ML)', 'Pet_GIF', 'Pet_PNG', 'Pet_RAW']
        # []
        # []
        # []
        # ['image(BigSize)']
        # []
        # ...
        
    for dir_name, sub_dir_list, file_names in os.walk(file_address):
        print(file_names)
        # 폴더 내부의 모든 파일들의 이름을 리스트로 반환
        # ['CSV&XLS.zip', 'csv.zip', 'image(BigSize).zip', 'images(ML).zip', 'Pet_GIF.zip', 'Pet_PNG.zip', 'Pet_RAW.zip', '붓꽃.csv']
        # ...
    ```

- 05-06 File처리1

    ``` python
    # 1. 파일 열기
    in_fp = open('C:/Windows/win.ini', 'r')
    out_fp = open('C:/images/new_win.ini', 'w')

    # 2. 파일 읽기, 또는 쓰기
    while True:
        in_str = in_fp.readline()
        if not in_str:
            break
        out_fp.writelines(in_str)

    # # 라인수가 적을 경우
    # in_str_list = in_fp.readlines()
    # print(in_str_list)
    # for line in in_str_list:
    #     print(line, end='')

    # 3. 파일 닫기
    in_fp.close()
    out_fp.close()
    print('ok')

    # # 파일 열고 수정하기
    # new_fp = open('C:/images/new_win.ini', 'r')

    # while True:
    #     in_str = new_fp.readline()
    #     if not in_str:
    #         break
    #     print(in_str, end='')

    # new_fp.close()

    ```

- 05-07 미션1 그림판

    ``` python
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
    ```

- 05-08 미션2 뷰어 확대, 축소
    ``` python
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.simpledialog

    # 함수 부분
    def func_open():
        global photo
        file_name = tk.filedialog.askopenfilename(
            parent=window, filetypes=(('GIF 파일', '*.gif'), ('모든 파일', '*.*')))
        
        photo = tk.PhotoImage(file=file_name)
        p_label.configure(image=photo)
        p_label.image = photo

    def func_exit():
        window.quit()
        window.destroy()

    def func_zoom_in():
        global photo
        value = tk.simpledialog.askinteger('확대하기', '배수를 입력해 주세요(2~8)', minvalue=2, maxvalue=8)
        photo = photo.zoom(value, value)
        p_label.configure(image=photo)
        p_label.image = photo

    def func_zoom_out():
        global photo
        value = tk.simpledialog.askinteger('축소하기', '배수를 입력해 주세요(2~8)', minvalue=2, maxvalue=8)
        photo = photo.subsample(value, value)
        p_label.configure(image=photo)
        p_label.image = photo

    # 변수 부분


    # 메인 코드
    if __name__ == "__main__":
        
        window = tk.Tk()
        window.geometry('400x400')
        window.title('명화 감상하기')
        
        photo = tk.PhotoImage()
        p_label = tk.Label(window, image=photo)
        p_label.pack(expand=1, anchor=tk.CENTER)

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='파일', menu=file_menu)
        effect_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='이미지 효과', menu=effect_menu)

        file_menu.add_cascade(label='파일 열기', command=func_open)
        file_menu.add_separator()
        file_menu.add_cascade(label='프로그램 종료', command=func_exit)

        effect_menu.add_cascade(label='확대하기', command=func_zoom_in)
        effect_menu.add_separator()
        effect_menu.add_cascade(label='축소하기', command=func_zoom_out)

        window.mainloop()
    ```

- 05-09 미션3 메모장

    ``` python
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.simpledialog

    # global variable
    file_name = ''

    # function
    def func_open():
        global file_name

        file_name = tk.filedialog.askopenfilename(
            parent=window, filetypes=(('텍스트 파일', '*.txt; *.ini; *.py'), ('모든 파일', '*.*')))

        with open(file_name, 'r') as rf:
            str_list = rf.readlines()
            memo_str = ''.join(str_list)
            text_label.insert(tk.END, memo_str)
        print('Open')
        

    def func_save():
        global file_name
        
        memo_str = text_label.get('1.0', tk.END)
        with open(file_name, 'w') as wf:
            wf.writelines(memo_str)
        print('Save')

    def func_change():
        old_str = tk.simpledialog.askstring('기존 문자', '기존 문자열:')
        new_str = tk.simpledialog.askstring('새 문자', '새 문자열:')
        memo_str = text_label.get('1.0', tk.END)
        memo_str = memo_str.replace(old_str, new_str)

        text_label.delete('1.0', tk.END)
        text_label.insert(tk.END, memo_str)

    def func_copy():
        global select_str
        select_str = text_label.selection_get()

    def func_paste():
        global select_str
        cur_pos = text_label.index(tk.INSERT)
        text_label.insert(cur_pos, select_str)


    # main
    if __name__ == "__main__":
        
        window = tk.Tk()
        window.title('notepad Beta (Ver0.01)')
        window.geometry('600x400')

        text_label = tk.Text(window, bg='white', width=50, height=50)
        text_label.pack(expand=1, anchor=tk.CENTER)

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)

        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='파일', menu=file_menu)
        edit_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='편집', menu=edit_menu)

        file_menu.add_cascade(label='파일 열기', command=func_open)
        file_menu.add_cascade(label='파일 저장', command=func_save)

        edit_menu.add_cascade(label='바꾸기', command=func_change)
        edit_menu.add_cascade(label='복사', command=func_copy)
        edit_menu.add_cascade(label='붙여넣기', command=func_paste)
        
        window.mainloop()
    ```


- 05-10 퀴즈 뷰어만들기
    ``` python
    import tkinter as tk

    # global variable
    NUM = 0
    dir_name = 'C:/images/Pet_GIF/Pet_GIF(256x256)/'
    f_name_list = ['cat01_256.gif',
        'cat02_256.gif',
        'cat03_256.gif',
        'cat04_256.gif',
        'cat05_256.gif',
        'cat06_256.gif']

    # function
    def func_next():
        global NUM
        NUM += 1
        if NUM >= len(f_name_list):
            NUM = 0
        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo

    def func_pre():
        global NUM
        NUM -= 1
        if NUM < 0:
            NUM = len(f_name_list)-1
        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo

    def func_home():
        global NUM
        NUM = 0

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo

    def func_end():
        global NUM
        NUM = len(f_name_list)-1

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo

    def func_key_press(event):
        global NUM, dir_name, f_name_list

        if event.keycode == 36:  # 'Home'
            NUM = 0
        elif event.keycode == 35:  # 'End'
            NUM = len(f_name_list) - 1
        elif 49 <= event.keycode <= 57:  # 1~9
            NUM += event.keycode - 48
            if NUM > len(f_name_list) -1:
                NUM = (NUM % len(f_name_list))

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo


    def func_skip(number):
        global NUM, dir_name, f_name_list
        NUM += number
        if NUM > len(f_name_list) -1:
            NUM = (NUM % len(f_name_list))

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label.config(image=photo)
        t_label.config(text=f_name_list[NUM])
        p_label.image = photo


    # main
    if __name__ == "__main__":
        
        window = tk.Tk()
        window.title('GIF Viewer Beta (Ver 0.02)')
        window.geometry('300x330')
        window.resizable(width=True, height=True)

        photo = tk.PhotoImage(file=dir_name+f_name_list[NUM])
        p_label = tk.Label(image=photo)
        t_label = tk.Label(text=f_name_list[NUM])

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        
        move_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='이동', menu=move_menu)
        skip_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='건너뛰기', menu=skip_menu)

        move_menu.add_cascade(label='앞으로', command=func_next)
        move_menu.add_cascade(label='뒤로', command=func_pre)

        skip_menu.add_cascade(label='1', command=lambda:func_skip(1))
        skip_menu.add_cascade(label='3', command=lambda:func_skip(3))
        skip_menu.add_cascade(label='5', command=lambda:func_skip(5))

        button1 = tk.Button(window, text='<-', command=func_pre)
        button2 = tk.Button(window, text='->', command=func_next)
        button3 = tk.Button(window, text='Home', command=func_home)
        button4 = tk.Button(window, text='End', command=func_end)

        p_label.place(x=15, y=50)
        t_label.place(x=90, y=10)

        button1.place(x=15, y=5)
        button2.place(x=250, y=5)
        button3.place(x=40, y=5)
        button4.place(x=219, y=5)

        window.bind("<Key>", func_key_press)

        window.mainloop()
    ```

## 과제

1. 그림판 만들기(p.325)
   - [도형] --> [선], [원]을 추가한 후 선을 선택하면 선이 그려지고, 원을 선택하면 원이 그려지기
2. 10번에 다음 기능을 추가(p.322)
3. 텍스트 파일 뷰어를 만들기
   - 메뉴 [파일] >> [열기]에서 텍스트 파일을 선택
   - 선택된 파일을 화면에 출력(Text 위젯 사용)
   - 파일의 내용을 변경
   - 메뉴 [파일] >> [저장]을 선택하면 파일이 저장됨
   - (선택) 메뉴에서 [편집]>>[바꾸기] 기능 구현
   - (선택) 메뉴에서 [편집]>>[복사],[붙여넣기] 기능 구현
4. Self Study 10-3 완성하기(p.303)
   - 버튼 추가하기
     - Home 버튼 --> 첫그림
     - End 버튼 --> 마지막 그림
     - -> 버튼 --> 다음그림
     - <- 버튼 --> 이전 그림
     - 숫자는 현재그림+숫자위치: 넘치면 마지막 그림
   - 메뉴 추가하기
     - ​[이동] --> [앞으로], [뒤로]
     - [건너뛰기] --> [1], [3], [5]
