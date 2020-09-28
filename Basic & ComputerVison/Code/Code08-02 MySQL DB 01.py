# Import
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import pymysql
import os
import math
import datetime
import tempfile

# Global Variable
IP_ADDR = '192.168.111.10'
USER_NAME = 'root'
USER_PW = '1234'
DB_NAME = 'bigdata_db'
CHAR_SET = 'utf8'


# Function
def select_file():
    file_name = tk.filedialog.askopenfilename(
        parent=window, filetype=(('RAW file', '*.raw'), ('All file', '*.*')))
    if file_name == '' or filedialog == None:
        return
    edt1.insert(0, str(file_name))


def upload_file():
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME,
        password=USER_PW, db=DB_NAME, charset=CHAR_SET)
    cur = con.cursor()

    full_name=edt1.get()
    with open(full_name, 'rb') as rfp:
        bin_data = rfp.read()

    fname = os.path.basename(full_name)
    fsize = os.path.getsize(full_name)
    height = width = int(math.sqrt(fsize))
    now = datetime.datetime.now()
    up_date = now.strftime('%Y-%m-%d')
    up_user = USER_NAME

    sql = ('INSERT INTO rawImage_TBL(raw_id, raw_height, raw_width, '
           'raw_fname, raw_update, raw_uploader, raw_avg, raw_data) '
           'VALUES(NULL, {}, {}, "{}", "{}", "{}", 0, %s);'
           .format(str(height), str(width), fname, up_date, up_user))

    print(sql)
    tuple_data = (bin_data,)
    cur.execute(sql, tuple_data)
    con.commit()
    cur.close()
    con.close()


def download_file():
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME,
        password=USER_PW, db=DB_NAME, charset=CHAR_SET)
    
    cur = con.cursor()
    sql = "SELECT raw_fname, raw_data FROM rawImage_TBL WHERE raw_id = 1"
    cur.execute(sql)

    fname, bin_data = cur.fetchone()
    full_path = tempfile.gettempdir() + '/' + fname
    with open(full_path, 'wb') as wfp:
        wfp.write(bin_data)

    print(full_path)  # C:\Users\wansang\AppData\Local\Temp\
    cur.close()
    con.close()
    print(sql)


# Main
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('500x200')
    window.title('Raw -> DB Ver0.01')
    
    edt1 = tk.Entry(window, width=50)
    edt1.pack()

    btn_file = tk.Button(window, text='Select File', command=select_file)
    btn_up_file = tk.Button(window, text='Upload', command=upload_file)
    btn_down_file = tk.Button(window, text='Download', command=download_file)

    btn_file.pack()
    btn_up_file.pack()
    btn_down_file.pack()

    window.mainloop()
