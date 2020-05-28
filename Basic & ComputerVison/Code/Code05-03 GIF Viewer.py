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
