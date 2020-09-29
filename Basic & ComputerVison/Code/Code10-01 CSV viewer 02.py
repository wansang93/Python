import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import csv

csv_list = []

def open_csv():
    global csv_list
    file_name = tk.filedialog.askopenfilename(parent=None,
        filetypes=(('csv file', '*.csv'), ('all file', '*.*')))

    with open(file_name) as rfp:
        reader = csv.reader(rfp)
        header_list = next(reader)
        for c_list in reader:
            csv_list.append(c_list)
    
    sheet.delete(*sheet.get_children())

    sheet.column('#0', width=70)
    sheet.heading('#0', text=header_list[0])

    sheet['column'] = header_list[1:]
    for col_name in header_list[1:]:
        sheet.column(col_name, width=70)
        sheet.heading(col_name, text=col_name)

    for row in csv_list:
        sheet.insert('', 'end', text=row[0], value=row[1:])

    sheet.pack(expand=1, anchor=tk.CENTER)

if __name__ == "__main__":

    window = tk.Tk()
    window.geometry('400x300')

    sheet = ttk.Treeview(window)

    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    file_menu = tk.Menu(main_menu)
    main_menu.add_cascade(label="CSV 처리", menu=file_menu)
    file_menu.add_command(label="CSV 열기", command=open_csv)

    window.mainloop()