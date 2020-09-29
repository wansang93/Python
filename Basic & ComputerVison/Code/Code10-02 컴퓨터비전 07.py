import tkinter as tk
import tkinter.simpledialog
import tkinter.filedialog
import os
import math
import matplotlib.pyplot as plt
import struct
# ==================== Global Variable ====================
window, canvas, paper = None, None, None
inH, inW, outH, outW = [0] * 4
inImage, outImage = [], []
filename = ''
VIEW_X, VIEW_Y = 512, 512
# ========== Mouse Event ==========
panYN = False
sx, sy, ex, ey = [0] * 4
# ========== Mask Value ==========
# embossing mask(0)
embossing = [
    [-1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]]
# blurring mask(1)
blurring = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]]
# sharpening mask(2)
sharpening = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]]
# edge detect mask(3)
edge_detect = [
    [0, 0, 0],
    [-1, 1, 0],
    [0, 0, 0]]
# gaussian mask(4)
gaussian = [
    [1/16, 1/8, 1/16],
    [1/8, 1/4, 1/8],
    [1/16, 1/8, 1/16]]
# high frequency(5)
high_freq = [
    [-1/9, -1/9, -1/9],
    [-1/9, 8/9, -1/9],
    [-1/9, -1/9, -1/9]]
# low frequency(6)
low_freq = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]]
mask_list = [embossing, blurring, sharpening, edge_detect, gaussian, high_freq, low_freq]

# ==================== Function Declaration ====================
# ========== file I/O ==========
# memory declaration
def malloc(h, w, init_value=0):
    reg_memory = []
    for _ in range(h):
        tem_list = []
        for _ in range(w):
            tem_list.append(init_value)
        reg_memory.append(tem_list)
    return reg_memory

# load image
def load_image(f_name):
    global inH, inW, outH, outW, inImage, outImage, filename
    # inH, inW값 넣기
    f_size = os.path.getsize(f_name)  # f_size = getsize(f_name)
    inH = inW = int(math.sqrt(f_size))  # only upload square image
    inImage = malloc(inH, inW)

    # 파일 -> 메모리
    with open(f_name, 'rb') as rFp:
        for i in range(inH):
            for k in range(inW):
                inImage[i][k] = int(ord(rFp.read(1)))  # ord()는 아스키 값을 읽는 함수, 반대는 chr()이다.

# open image
def open_image():
    global inH, inW, outH, outW, inImage, outImage, filename
    filename = tkinter.filedialog.askopenfilename(
        parent=window, filetype=(('RAW file', '*.raw'), ('All file', '*.*')))
    if filename == '' or filename is None:
        return
    
    load_image(filename)
    equal_image()

# save image
def save_image():
    global inH, inW, outH, outW, inImage, outImage, filename
    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window, mode='wb', defaultextension='*.raw', filetype=(('RAW file', '*.raw'), ('All file', '*.*')))
    if save_fp == '' or save_fp == None:
        return
    
    for i in range(outH):
        for j in range(outW):
            save_fp.write(struct.pack('B', outImage[i][j]))
    save_fp.close()


# display image
def display_image():
    global inH, inW, outH, outW, inImage, outImage, filename, window, canvas, paper
    global VIEW_X, VIEW_Y
    if canvas is not None:
        canvas.destroy()

    if outH <= VIEW_Y or outW <= VIEW_X:
        VIEW_X = outW
        VIEW_Y = outH
        step_X, step_Y = 1, 1
    else:
        step_X = outW / VIEW_X
        step_Y = outH / VIEW_Y

    canvas = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, relief='solid', bd=0, bg='white')
    paper = tk.PhotoImage(height=outH, width=outW)
    canvas.create_image((outH//2, outW//2), image=paper, state='normal', anchor=tk.CENTER)

    # for i in range(outH):
    #     for k in range(outW):
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    # 성능 개선
    import numpy as np
    rgb_str = ''
    for i in np.arange(0, outH, step_Y):
        tmp_str = ''
        for k in np.arange(0, outW, step_X):
            i = int(i)
            k = int(k)
            r = g = b = outImage[i][k]
            tmp_str += ' #{:02x}{:02x}{:02x}'.format(r, g, b)
        rgb_str += '{{{}}} '.format(tmp_str)
    paper.put(rgb_str)

    canvas.bind('<Button-1>', mouse_click)
    canvas.bind('<ButtonRelease-1>', mouse_drop)
    canvas.pack(expand=1, anchor=tk.CENTER)
    VIEW_X, VIEW_Y = 512, 512

# ========== Vision Algorithm ==========
# equal image
def equal_image():
    global inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = malloc(outH, outW)

    for i in range(outH):
        for k in range(outW):
            outImage[i][k] = inImage[i][k]

    display_image()

# bright control(+/-)
def add_image():
    global inH, inW, outH, outW, inImage, outImage
    value = tkinter.simpledialog.askinteger('bright +/-', '(-255~255)', minvalue=-255, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            v = inImage[i][k] + value
            if v > 255:
                v = 255
            elif v < 0:
                v = 0
            outImage[i][k] = v

    display_image()

# reverse image
def rev_image():
    global inH, inW, outH, outW, inImage, outImage
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - inImage[i][k]

    display_image()

def para_image():
    global inH, inW, outH, outW, inImage, outImage
    LUT = [0 for _ in range(256)]
    for input in range(256):
        LUT[input] = int(255 - 255 * math.pow(input/128-1, 2))

    for i in range(inH):
        for k in range(inW):
            input = inImage[i][k]
            outImage[i][k] = LUT[inImage[i][k]]

    display_image()

def bw_image():
    global inH, inW, outH, outW, inImage, outImage
    mysum = 0
    for i in range(inH):
        for k in range(inW):
            mysum += inImage[i][k]
    avg = mysum // (inW * inH)

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] > avg:
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0

    display_image()

# ========== Vision Algorithm(0.02) ==========
# Move Display
def move_image():
    global panYN
    panYN = True
    canvas.configure(cursor='mouse')

def mouse_click(event):
    global sx, sy, ex, ey, panYN
    if panYN is False:
        return
    sx = event.x
    sy = event.y

def mouse_drop(event):
    global inH, inW, outH, outW, inImage, outImage
    global sx, sy, ex, ey, panYN
    if panYN is False:
        return
    ex = event.x
    ey = event.y
    mx = sx - ex
    my = sy - ey
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255
    for i in range(inH):
        for k in range(inW):
            if 0 <= i-my < outW and 0 <= k-mx < outH:
                outImage[i-my][k-mx] = inImage[i][k]
    panYN = False

    display_image()

# upside-down
def up_down_image():
    global inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    for i in range(inH):
        for k in range(inW):
            outImage[inH-i-1][k] = inImage[i][k]

    display_image()

# zoom-out(평균변환)
def zoom_out_image2():
    global inH, inW, outH, outW, inImage, outImage
    scale = tkinter.simpledialog.askinteger('zoom_out', '(2~16)', minvalue=2, maxvalue=16)
    outH = inH//scale
    outW = inW//scale
    outImage = []
    outImage = malloc(outH, outW)

    for i in range(inH):
        for k in range(inW):
            outImage[i//scale][k//scale] += inImage[i][k]
    for i in range(outH):
        for k in range(outW):
            outImage[i][k] //= (scale*scale)

    display_image()

# zoom-in(양선형 보간)
def zoom_in_image2():
    global inH, inW, outH, outW, inImage, outImage
    scale = tkinter.simpledialog.askinteger('zoom_in', '(2~8)', minvalue=2, maxvalue=8)
    outH = inH * scale
    outW = inW * scale
    outImage = []
    outImage = malloc(outH, outW)

    for i in range(outH):
        for k in range(outW):
            # 실수위치 및 정수위치
            rH = i / scale
            rW = k / scale
            iH = int(rH)
            iW = int(rW)
            # 실수와 정수의 차이값
            x = rW - iW
            y = rH - iH

            if 0 <= iH < inH - 1 and 0 <= iW < inW - 1:
                # 결정할 위치(N)의 상하좌우 픽셀
                C1 = inImage[iH][iW]
                C2 = inImage[iH][iW + 1]
                C3 = inImage[iH + 1][iW + 1]
                C4 = inImage[iH + 1][iW]
                newValue = C1 * (1 - y) * (1 - x) + C2 * (1 - y) * x + C3 * y * x + C4 * y * (1 - x)
                outImage[i][k] = int(newValue)

    display_image()

# zoom-out
def zoom_out_image():
    global inH, inW, outH, outW, inImage, outImage
    scale = tkinter.simpledialog.askinteger('zoom_out', '(2~16)', minvalue=2, maxvalue=16)
    outH = inH//scale
    outW = inW//scale
    outImage = []
    outImage = malloc(outH, outW)

    for i in range(outH):
        for k in range(outW):
            outImage[i][k] = inImage[i*scale][k*scale]

    display_image()

# zoom-in
def zoom_in_image():
    global inH, inW, outH, outW, inImage, outImage
    scale = tkinter.simpledialog.askinteger('zoom_in', '(2~8)', minvalue=2, maxvalue=8)
    outH = inH*scale
    outW = inW*scale
    outImage = []
    outImage = malloc(outH, outW)

    for i in range(outH):
        for k in range(outW):
            outImage[i][k] = inImage[i//scale][k//scale]

    display_image()

# rotate
def rotate_image():
    global inH, inW, outH, outW, inImage, outImage
    angle = tkinter.simpledialog.askinteger('rotate', '(1~360)', minvalue=1, maxvalue=360)
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    radian = angle * math.pi / 180
    cx = inW // 2
    cy = inH // 2
    for i in range(inH):
        for k in range(inW):
            xs = i
            ys = k
            xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy)) + cx
            yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy)) + cy
            if 0 <= xd < outH and 0 <= yd < outW:
                outImage[xs][ys] = inImage[xd][yd]
            else:
                outImage[xs][ys] = 255

    display_image()

# histogram
def histogram_image():
    global inH, inW, outH, outW, inImage, outImage
    incountlist = [0] * 256
    outcountlist = [0] * 256

    for i in range(inH):
        for k in range(inW):
            incountlist[inImage[i][k]] += 1

    for i in range(outH):
        for k in range(outW):
            outcountlist[outImage[i][k]] += 1

    plt.plot(incountlist)
    plt.plot(outcountlist)
    plt.show()

# stretch
def stretch_image():
    global inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    max_val = min_val = inImage[0][0]
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < min_val:
                min_val = inImage[i][k]
            elif inImage[i][k] > max_val:
                max_val = inImage[i][k]
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = int(((inImage[i][k] - min_val) / (max_val - min_val)) * 255)

    display_image()

# end_in
def end_in_image():
    global inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    max_val = min_val = inImage[0][0]
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < min_val:
                min_val = inImage[i][k]
            elif inImage[i][k] > max_val:
                max_val = inImage[i][k]

    min_add = tkinter.simpledialog.askinteger('min_add', '(0~255)', minvalue=0, maxvalue=255)
    max_add = tkinter.simpledialog.askinteger('max_add', '(0~255)', minvalue=0, maxvalue=255)

    min_val += min_add
    max_val -= max_add

    for i in range(inH):
        for k in range(inW):
            value = int(((inImage[i][k] - min_val) / (max_val - min_val)) * 255)
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            outImage[i][k] = value

    display_image()

# equalize
def equalize_image():
    global inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    histo = [0] * 256
    sum_histo = [0] * 256
    normal_histo = [0] * 256
    # 히스토그램
    for i in range(inH):
        for k in range(inW):
            histo[inImage[i][k]] += 1
    # 누적히스토그램
    sValue = 0
    for i in range(len(histo)):
        sValue += histo[i]
        sum_histo[i] = sValue
    # 정규화 누적 히스토그램
    for i in range(len(sum_histo)):
        normal_histo[i] = int(sum_histo[i] / (inW*inH) * 255)
    # 영상처리
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = normal_histo[inImage[i][k]]

    display_image()
# ========== Vision Algorithm(0.02) Endline ==========
# ========== Vision Algorithm(0.03) ==========
# Mask Processing
def mask_image(mask_number):
    global inH, inW, outH, outW, inImage, outImage
    global mask_list
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    m_size = 3
    mask = mask_list[mask_number]
    # 임시 입력영상 메모리 확보
    tmp_in_image = malloc(inH+m_size-1, inW+m_size-1, 127)
    tmp_out_image = malloc(outH, outW)
    # 원 입력 -> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmp_in_image[i+m_size//2][k+m_size//2] = inImage[i][k]
    # 회선연산
    for i in range(m_size//2, inH + m_size//2):
        for k in range(m_size//2, inW + m_size//2):
            # 각 점을 처리
            S = 0.0
            for m in range(0, m_size):
                for n in range(0, m_size):
                    S += mask[m][n]*tmp_in_image[i+m-m_size//2][k+n-m_size//2]
            tmp_out_image[i-m_size//2][k-m_size//2] = S
    # 127 더하기
    if mask_number == 0:
        for i in range(outH):
            for k in range(outW):
                tmp_out_image[i][k] += 127
    # 임시 출력 -> 원 출력
    for i in range(outH):
        for k in range(outW):
            value = tmp_out_image[i][k]
            if value > 255:
                value = 255
            elif value < 0:
                value = 0
            outImage[i][k] = int(value)

    display_image()
# ========== Vision Algorithm(0.03) Endline ==========
# ========== Vision Algorithm(0.04) ==========
def morph_image():
    global window, canvas, paper, filename, inH, inW, outH, outW, inImage, outImage
    outH = inH
    outW = inW
    outImage = []
    outImage = malloc(outH, outW)
    # 추가 영상 선택
    filename2 = tk.filedialog.askopenfilename(parent=window,
        filetypes=(("RAW file", "*.raw"), ("All file", "*.*")))
    if filename2 == '' or filename2 is None:
        return

    fsize = os.path.getsize(filename2)  # 파일의 크기(바이트)
    inH2 = inW2 = int(math.sqrt(fsize))  # 핵심 코드

    # 입력영상 메모리 확보
    inImage2 = []
    inImage2 = malloc(inH2, inW2)

    # 파일 --> 메모리
    with open(filename2, 'rb') as rFp:
        for i in range(inH2):
            for k in range(inW2):
                inImage2[i][k] = int(ord(rFp.read(1)))

    import threading
    import time

    def morp_func():
        w1 = 1
        w2 = 0
        for _ in range(20):
            for i in range(inH):
                for k in range(inW):
                    new_value = int(inImage[i][k]*w1 + inImage2[i][k]*w2)
                    if new_value > 255:
                        new_value = 255
                    elif new_value < 0:
                        new_value = 0
                    outImage[i][k] = new_value
            display_image()
            w1 -= 0.05
            w2 += 0.05
            time.sleep(0.5)

    threading.Thread(target=morp_func).start()
# ========== Vision Algorithm(0.04) Endline ==========
# ========== Vision Algorithm(0.05) ==========
# histogram_custom
def histogram_image_custom():
    global inH, inW, outH, outW, inImage, outImage
    outcountlist = [0] * 256
    normalcountlist = [0] * 256

    # 빈도수 계산
    for i in range(outH):
        for k in range(outW):
            outcountlist[outImage[i][k]] += 1
    max_val = max(outcountlist)
    min_val = min(outcountlist)
    HIGH = 256

    # 정규화 (카운트 값 - 최솟값) * HIGH / (최댓값 - 최솟값)
    for i in range(len(outcountlist)):
        normalcountlist[i] = (outcountlist[i] - min_val) * HIGH / (max_val - min_val)

    # 서브 윈도우에 만들기
    sub_window = tk.Toplevel(window)
    sub_window.geometry('256x256')
    sub_canvas = tk.Canvas(sub_window, width=256, height=256)
    sub_paper = tk.PhotoImage(width=256, height=256)
    sub_canvas.create_image((256//2, 256//2), image=sub_paper, state='normal')

    # 서브 윈도우 출력
    for i in range(len(normalcountlist)):
        for k in range(int(normalcountlist[i])):
            data = 0
            sub_paper.put('#{:02x}{:02x}{:02x}'.format(data, data, data), (i, 255-k))
    sub_canvas.pack(expand=1, anchor=tk.CENTER)
    sub_window.mainloop()
# ========== Vision Algorithm(0.05) Endline ==========
# ========== Vision Algorithm(0.06) ==========
import pymysql
import tempfile
import random
import datetime


# Global Variable
IP_ADDR = '192.168.111.10'
USER_NAME = 'root'
USER_PW = '1234'
DB_NAME = 'bigdata_db'
CHAR_SET = 'utf8'
raw_file_list = []


def save_temp_image():
    global outH, outW, outImage, raw_file_list
    save_fp = f'{tempfile.gettempdir()}/{str(random.randint(10000, 99999))}.raw'
    if save_fp == '' or save_fp is None:
        return
    with open(save_fp, mode='wb') as sf:
        for i in range(outH):
            for j in range(outW):
                sf.write(struct.pack('B', outImage[i][j]))
    return save_fp


# Get avg, max, min
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

def upload_mysql():
    global raw_file_list

    if inImage == []:
        tkinter.messagebox.showinfo(title='Error',
            message='Please open image frist')
        return

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

    # raw_file_list check
    if raw_file_list:
        raw_file_list = []
    raw_file_list.append(save_temp_image())

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

        # 서버로 보내기
        cur.execute(sql, (bin_data,))
        con.commit()

    # 서버 종료
    cur.close()
    con.close()


def download_mysql():
    # DB 연결
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME,
        password=USER_PW, db=DB_NAME, charset=CHAR_SET)
    cur = con.cursor()

    sql = ('SELECT raw_id, raw_fname, raw_extname, '
           'raw_height, raw_width FROM rawimage_tbl')
    cur.execute(sql)

    query_list = cur.fetchall()
    row_list = [f'{data[0]}:{data[1]}.{data[2]}:{data[3]}x{data[4]}' for data in query_list]

    def select_record():
        sel_index = list_box.curselection()[0]
        sub_window.destroy()
        raw_id = query_list[sel_index][0]

        sql = ('SELECT raw_fname, raw_extname, raw_data '
               f'FROM rawimage_tbl WHERE raw_id = {str(raw_id)}')
        cur.execute(sql)
        
        f_name, ext_name, bin_data = cur.fetchone()
        full_path = f'{tempfile.gettempdir()}/{f_name}.{ext_name}'

        with open(full_path, 'wb') as wfp:
            wfp.write(bin_data)

        cur.close()
        con.close()

        load_image(full_path)
        equal_image()

    # 서브 윈도우 생성
    sub_window = tk.Toplevel(window)
    sub_window.geometry('200x200')
    scrollbar = tk.Scrollbar(sub_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    list_box = tk.Listbox(sub_window, yscrollcommand=scrollbar.set)
    button = tk.Button(sub_window, text='선택', command=select_record)

    for row_str in row_list:
        list_box.insert(tk.END, row_str)

    list_box.pack(fill=tk.BOTH)
    scrollbar.config(command=list_box.yview_moveto)
    button.pack(anchor=tk.CENTER)
    sub_window.mainloop()
    
    # 서버 종료
    cur.close()
    con.close()
# ========== Vision Algorithm(0.06) Endline ==========
# ========== Vision Algorithm(0.07) ==========
import csv
def save_as_csv():
    global window, outImage, outH, outW
    if outImage == []:
        tkinter.messagebox.showinfo(title='Error',
            message='Please open image frist')
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window, filetype=(('CSV file', '*.csv'), ('All file', '*.*')))
    if save_fp == '' or save_fp is None:
        return

    with open(save_fp.name, 'w', newline='') as wfp:
        csv_writer = csv.writer(wfp)
        for i in range(outH):
            for j in range(outW):
                row_list = [i, j, outImage[i][j]]
                csv_writer.writerow(row_list)


def open_csv():
    global window, filename
    filename = tkinter.filedialog.askopenfilename(
        parent=window, filetype=(('CSV file', '*.csv'), ('All file', '*.*')))
    if filename == '' or filename is None:
        return
    
    load_csv(filename)
    equal_image()


def load_csv(f_name):
    global window, canvas, paper, filename, inH, inW, outH, outW, inImage, outImage
    f_size = 0
    with open(f_name, 'r') as rfp:
        for _ in rfp:
            f_size += 1
    inH = inW = int(math.sqrt(f_size))
    inImage = malloc(inH, inW)

    with open(f_name, 'r') as rfp:
        for row_list in rfp:
            col, row, value = map(int, row_list.strip().split(','))
            inImage[col][row] = value
# ========== Vision Algorithm(0.07) Endline ==========


# ==================== Main code ====================
if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('600x600')
    window.title('Computer Vision (Ver 0.07)')

    canvas = tk.Canvas(window, height=512, width=512, relief='solid', bd=2, bg='white')
    canvas.pack(expand=1, anchor=tk.CENTER)

    mainMenu = tk.Menu(window)
    window.config(menu=mainMenu)

    fileMenu = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label='Open RAW file', command=open_image)
    fileMenu.add_separator()
    fileMenu.add_command(label='Save file', command=save_image)

    comVisionMenu1 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Pixel', menu=comVisionMenu1)
    comVisionMenu1.add_command(label='Brighten/Darken', command=add_image)
    comVisionMenu1.add_command(label='Contrast', command=rev_image)
    comVisionMenu1.add_command(label='parabola', command=para_image)
    comVisionMenu1.add_separator()
    comVisionMenu1.add_command(label="morphing_image", command=morph_image)

    comVisionMenu2 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Geometry', menu=comVisionMenu2)
    comVisionMenu2.add_command(label='Black&White', command=bw_image)
    comVisionMenu2.add_command(label='zoom_out(better)', command=zoom_out_image2)
    comVisionMenu2.add_command(label='zoom_in(better)', command=zoom_in_image2)
    comVisionMenu2.add_separator()
    comVisionMenu2.add_command(label='Histogram', command=histogram_image)
    comVisionMenu2.add_command(label='Histogram_custom', command=histogram_image_custom)
    comVisionMenu2.add_command(label='Stretch', command=stretch_image)
    comVisionMenu2.add_command(label='End_In', command=end_in_image)
    comVisionMenu2.add_command(label='Equalize', command=equalize_image)

    comVisionMenu3 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Geometry', menu=comVisionMenu3)
    comVisionMenu3.add_command(label='Up_Down', command=up_down_image)
    comVisionMenu3.add_command(label='Move', command=move_image)
    comVisionMenu3.add_command(label='zoom_out', command=zoom_out_image)
    comVisionMenu3.add_command(label='zoom_in', command=zoom_in_image)
    comVisionMenu3.add_command(label='Rotate', command=rotate_image)

    comVisionMenu4 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Area', menu=comVisionMenu4)
    comVisionMenu4.add_command(label='embossing', command=lambda: mask_image(0))
    comVisionMenu4.add_command(label='blurring', command=lambda: mask_image(1))
    comVisionMenu4.add_command(label='sharpening', command=lambda: mask_image(2))
    comVisionMenu4.add_command(label='edge detect', command=lambda: mask_image(3))
    comVisionMenu4.add_command(label='gaussian', command=lambda: mask_image(4))
    comVisionMenu4.add_command(label='high freq', command=lambda: mask_image(5))
    comVisionMenu4.add_command(label='low freq', command=lambda: mask_image(6))

    comVisionMenu5 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='etc', menu=comVisionMenu5)
    comVisionMenu5.add_command(label='Upload in MySQL', command=upload_mysql)
    comVisionMenu5.add_command(label='Download from MySQL', command=download_mysql)
    comVisionMenu5.add_command(label='Save as CSV file', command=save_as_csv)
    comVisionMenu5.add_command(label='Open CSV file', command=open_csv)
    
    window.mainloop()
