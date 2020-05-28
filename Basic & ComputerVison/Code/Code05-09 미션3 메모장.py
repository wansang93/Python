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
