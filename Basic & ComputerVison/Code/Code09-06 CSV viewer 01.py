import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x300')

sheet = ttk.Treeview(window)

# 첫 번째 열 해더 만들기
sheet.column('#0', width=70)  # 첫 번째 칼럼 내부 이름
sheet.heading('#0', text='제목1')

# 두 번째 열 이후 해더 만들기
sheet['columns'] = ('a', 'b', 'c')
sheet.column('a', width=70)
sheet.column('b', width=70)
sheet.column('c', width=70)

sheet.heading('a', text='제목2')
sheet.heading('b', text='제목3')
sheet.heading('c', text='제목4')
sheet.pack()

# 내용 채우기
sheet.insert('', 'end', text='1열1값', value=('1열1값', '1열2값', '1열3값'))
sheet.insert('', 'end', text='2열1값', value=('2열2값', '2열2값', '2열3값'))
sheet.insert('', 'end', text='3열1값', value=('3열3값', '3열2값', '3열3값'))

window.mainloop()