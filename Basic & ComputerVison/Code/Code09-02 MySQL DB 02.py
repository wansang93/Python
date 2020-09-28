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
raw_file_list = []


# Function
def select_file():
    global raw_file_list
    file_name = tk.filedialog.askopenfilename(
        parent=window, filetype=(('RAW file', '*.raw'), ('All file', '*.*')))
    if file_name == '' or filedialog == None:
        return
    edt1.insert(0, str(file_name))


    if raw_file_list:
        raw_file_list = []

    raw_file_list.append(file_name)
    print(raw_file_list)


def select_folder():
    global raw_file_list
    foldername = tk.filedialog.askdirectory(parent=window)
    if foldername == '' or foldername is None:
        return
    edt1.insert(0, str(foldername))
    # 파일 목록 뽑기
    raw_file_list = []
    for dirName, _, fnames in os.walk(foldername):
        for fname in fnames:
            _, extname = os.path.basename(fname).split('.')
            if extname.upper().strip() == 'RAW':
                raw_file_list.append(os.path.join(dirName, fname))
    print(raw_file_list)


# Version 0.02 개선
def upload_file():
    global raw_file_list

    # DB 연결
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME,
        password=USER_PW, db=DB_NAME, charset=CHAR_SET)
    cur = con.cursor()

    # DB 테이블 확인
    try:
        sql = ('CREATE TABLE rawimage_tbl (raw_id INT AUTO_INCREMENT PRIMARY KEY, '
               'raw_height smallint, raw_width smallint, raw_fname VARCHAR(30), raw_extname CHAR(5), '
               'raw_update DATE, raw_uploader VARCHAR(20), raw_avg TINYINT UNSIGNED, '
               'raw_max TINYINT UNSIGNED, raw_min TINYINT UNSIGNED, raw_data LONGBLOB);')
        cur.execute(sql)
    except:
        pass

    # 파일 읽기
    for full_name in raw_file_list:
        with open(full_name, 'rb') as rfp:
            bin_data = rfp.read()

        # 값들 추출하기
        fname, extname = os.path.basename(full_name).split('.')
        fsize = os.path.getsize(full_name)
        height = width = int(math.sqrt(fsize))
        now = datetime.datetime.now()
        up_date = now.strftime('%Y-%m-%d')
        up_user = USER_NAME
        avg, max_val, min_val = find_state(full_name, height, width)

        # sql 작성
        sql = ('INSERT INTO rawimage_tbl(raw_id, raw_height, raw_width, '
               'raw_fname, raw_extname, raw_update, raw_uploader, raw_avg, raw_max, raw_min, raw_data) '
               f'VALUES(NULL, {str(height)}, {str(width)}, '
               f'"{fname}", "{extname}", "{up_date}", "{up_user}", {avg}, {max_val}, {min_val}, %s);')
        print(sql)

        # 서버로 보내기
        cur.execute(sql, (bin_data,))
        con.commit()

    # 서버 종료
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

    print(full_path)
    cur.close()
    con.close()
    print(sql)

def malloc(height, width):
    ret_memory = [[0 for _ in range(width)] for _ in range(height)]
    return ret_memory


def find_state(full_name, height, width):
    in_image = malloc(height, width)
    with open(full_name, 'rb') as rfp:
        for i in range(height):
            for j in range(width):
                in_image[i][j] = int(ord(rfp.read(1)))

    sum_val = 0
    max_val = min_val = in_image[0][0]
    for i in range(height):
        for j in range(width):
            value = in_image[i][j]
            if min_val > value:
                min_val = value
            if max_val < value:
                max_val = value
            sum_val += value
    avg = sum_val // (height * width)

    return avg, max_val, min_val


# Main
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('500x200')
    window.title('Raw -> DB Ver0.02')
    
    edt1 = tk.Entry(window, width=50)
    edt1.pack()

    btn_file = tk.Button(window, text='Select File', command=select_file)
    btn_folder = tk.Button(window, text='Select Folder', command=select_folder)
    btn_up_file = tk.Button(window, text='Upload', command=upload_file)
    btn_down_file = tk.Button(window, text='Download', command=download_file)

    btn_file.pack()
    btn_folder.pack()
    btn_up_file.pack()
    btn_down_file.pack()

    window.mainloop()
