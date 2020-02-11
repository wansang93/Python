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
