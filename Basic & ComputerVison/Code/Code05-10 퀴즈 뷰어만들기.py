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
