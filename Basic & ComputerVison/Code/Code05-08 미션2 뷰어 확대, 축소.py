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
