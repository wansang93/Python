import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import csv
import xlrd

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


def open_excel():
    global csv_list
    filename = tk.filedialog.askopenfilename(
        parent=None,
        filetypes=(('excel file', '*.xls;*.xlsx'), ('all file', '*.*')))

    # workbook 만들기
    workbook = xlrd.open_workbook(filename)
    ws_list = workbook.sheets()

    header_list = []
    # 헤더리스트 만들기
    for i in range(ws_list[0].ncols):
        header_list.append(ws_list[0].cell_value(0, i))
    
    csv_list = []
    # 헤더리스트를 제외한 csv_list 만들기
    for wsheet in ws_list:
        row_count = wsheet.nrows
        col_count = wsheet.ncols
        for i in range(1, row_count):
            tmp_list = []
            for j in range(col_count):
                tmp_list.append(wsheet.cell_value(i, j))
            csv_list.append(tmp_list)

    sheet.delete(*sheet.get_children())

    # 0열 0행 채우기
    sheet.column('#0', width=70)
    sheet.heading('#0', text=header_list[0])

    # 0열 나머지 채우기
    sheet['columns'] = header_list[1:]
    for name in header_list[1:]:
        sheet.column(name, width=70)
        sheet.heading(name, text=name)
    
    # 1열부터 ~ 나머지 채우기
    for row in csv_list:
        sheet.insert('', 'end', text=row[0], values=row[1:])
    
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
    file_menu.add_command(label="Excel 열기", command=open_excel)

    window.mainloop()