import csv
import datetime
import math
import os
import random
import struct
import tempfile
import threading
import time
import tkinter.filedialog
import tkinter.messagebox
import tkinter.simpledialog
import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
import pymysql
import xlrd
import xlsxwriter

# ==================== Global Variable ====================
window, canvas, paper = None, None, None
in_h, in_w, in_image = 0, 0, []
out_h, out_w, out_image = 0, 0, []
file_name = ''
VIEW_X, VIEW_Y = 512, 512
# ========== Mouse Event ==========
pan_yn = False
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
mask_list = [
    embossing, blurring, sharpening, edge_detect, gaussian, high_freq, low_freq]
# ========== Server default ==========
IP_ADDR = '192.168.111.10'
USER_NAME = 'root'
USER_PW = '1234'
DB_NAME = 'bigdata_db'
CHAR_SET = 'utf8'
raw_file_list = []


# ==================== Function Declaration ====================
# ========== Bug Check ==========
def is_open_file(file_name):
    if not file_name:
        status.configure(text='Open is failed. Please try again')
        return False
    return True


def is_save_file(file_name):
    if not file_name:
        status.configure(text=f'Save is failed. Please try again')
        return False
    return True


def is_empty_image():
    global out_image
    if len(out_image) == 0:
        tkinter.messagebox.showinfo(
            title='Error',
            message='The image is empty, Please open image')
        return True
    return False


# ========== file I/O ==========
# memory allocation
def malloc(h, w, initvalue=0):
    ret_memory = [[initvalue for _ in range(w)] for _ in range(h)]
    return ret_memory


# open image
def open_image():
    global window, file_name
    file_name = 'D:/☆☆☆멀캠생활/Image/Pet_RAW(256x256)/cat01_256.raw'
    # file_name = tkinter.filedialog.askopenfilename(
    #     parent=window,
    #     filetypes=(('RAW file', '*.raw'), ('All file', '*.*')),
    # )
    if not is_open_file(file_name):
        return

    load_image(file_name)
    equal_image()
    display_image()


# load image
def load_image(file_name):
    global in_h, in_w, in_image
    f_size = os.path.getsize(file_name)  # f_size = getsize(filename)
    # only upload a square image
    # in_h, in_w값 넣기
    in_h = int(math.sqrt(f_size))
    in_w = int(math.sqrt(f_size))
    in_image = malloc(in_h, in_w)

    # 파일 -> 메모리
    with open(file_name, 'rb') as rFp:
        for i in range(in_h):
            for k in range(in_w):
                # ord()는 아스키 값을 읽는 함수, 반대는 chr()이다.
                in_image[i][k] = int(ord(rFp.read(1)))


# display out image
def display_image():
    global window, canvas, paper, file_name
    global in_h, in_w, in_image, out_h, out_w, out_image
    global VIEW_X, VIEW_Y
    if canvas:
        canvas.destroy()

    canvas = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, bg='white')
    paper = tk.PhotoImage(height=out_h, width=out_w)
    canvas.create_image(
        ((out_h//2)+2, (out_w//2)+2), image=paper, anchor=tk.CENTER)
    step_x, step_y = 1, 1
    if out_h > VIEW_Y:
        step_y = out_h / VIEW_Y
    if out_w > VIEW_X:
        step_x = out_w / VIEW_X

    # for i in range(out_h):
    #     for k in range(out_w):
    #         r = g = b = out_image[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    # 성능 개선
    rgb_str = ''
    for i in np.arange(0, out_h, step_y):
        i = int(i)
        tmp_str = ''
        for j in np.arange(0, out_w, step_x):
            j = int(j)
            r = g = b = int(out_image[i][j])
            tmp_str += f' #{r:02x}{g:02x}{b:02x}'
        rgb_str += f'{{{tmp_str}}} '
    paper.put(rgb_str)

    canvas.bind('<Button-1>', mouse_click)
    canvas.bind('<ButtonRelease-1>', mouse_drop)
    canvas.pack(expand=1, anchor=tk.CENTER)

    status.configure(
        text=f'({file_name}) In: {in_h}x{in_w}, Out: {out_h}x{out_w}',
    )


# save image
def save_image():
    global out_h, out_w, out_image, window
    if is_empty_image():
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window,
        mode='wb',
        defaultextension='*.raw',
        filetypes=(('RAW file', '*.raw'), ('All file', '*.*')),
    )
    if not is_save_file(save_fp):
        return

    status.configure(text=f'Image is being saved at {save_fp.name}')
    for i in range(out_h):
        for j in range(out_w):
            save_fp.write(struct.pack('B', out_image[i][j]))
    status.configure(text=f'Image is saved at {save_fp.name}')
    save_fp.close()


# ========== Vision Algorithm(0.01) ==========
# equal image
def equal_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = malloc(out_h, out_w)

    for i in range(out_h):
        for k in range(out_w):
            out_image[i][k] = in_image[i][k]


# bright control(+/-)
def add_image():
    global in_h, in_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    value = tkinter.simpledialog.askinteger(
        'bright +/-',
        '(-255~255)',
        minvalue=-255,
        maxvalue=255
    )
    for i in range(in_h):
        for k in range(in_w):
            v = int(in_image[i][k] + value)
            if v > 255:
                v = 255
            elif v < 0:
                v = 0
            out_image[i][k] = v

    display_image()


# invert image
def invert_image():
    global in_h, in_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    for i in range(in_h):
        for k in range(in_w):
            out_image[i][k] = 255 - in_image[i][k]

    display_image()


# parabola image
def para_image():
    global in_h, in_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    LUT = [0 for _ in range(256)]
    for value in range(256):
        LUT[value] = int(255 - 255 * math.pow(value / 128 - 1, 2))

    for i in range(in_h):
        for k in range(in_w):
            out_image[i][k] = LUT[in_image[i][k]]

    display_image()


# black & white image
def bw_image():
    global in_h, in_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    sum_value = 0
    for i in range(in_h):
        for k in range(in_w):
            sum_value += in_image[i][k]
    avg = sum_value // (in_w * in_h)

    for i in range(in_h):
        for k in range(in_w):
            if in_image[i][k] > avg:
                out_image[i][k] = 255
            else:
                out_image[i][k] = 0

    display_image()


# ========== Vision Algorithm(0.02) ==========
# Move Display
def move_image():
    global pan_yn, canvas
    if is_empty_image():
        return

    pan_yn = True
    canvas.configure(cursor='mouse')


def mouse_click(event):
    global sx, sy, ex, ey, pan_yn
    if not pan_yn:
        return
    sx = event.x
    sy = event.y


def mouse_drop(event):
    global in_h, in_w, out_h, out_w, in_image, out_image
    global sx, sy, ex, ey, pan_yn
    if not pan_yn:
        return

    mx = sx - event.x
    my = sy - event.y
    for i in range(in_h):
        for k in range(in_w):
            out_image[i][k] = 255

    for i in range(in_h):
        for k in range(in_w):
            if 0 <= i - my < out_w and 0 <= k - mx < out_h:
                out_image[i - my][k - mx] = in_image[i][k]
    pan_yn = False

    display_image()


# upside-down
def up_down_image():
    global in_h, in_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    for i in range(in_h):
        for k in range(in_w):
            out_image[in_h-i-1][k] = in_image[i][k]

    display_image()


# zoom-out(image averaging)
def zoom_out_image2():
    global in_h, in_w, out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_out', '(2~16)', minvalue=2, maxvalue=16)
    out_h = in_h // scale
    out_w = in_w // scale
    out_image = []
    out_image = malloc(out_h, out_w)

    for i in range(in_h):
        for k in range(in_w):
            out_image[i // scale][k // scale] += in_image[i][k]
    for i in range(out_h):
        for k in range(out_w):
            out_image[i][k] //= (scale * scale)

    display_image()


# zoom-in(bilinear interpolation)
def zoom_in_image2():
    global in_h, in_w, out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_in', '(2~8)', minvalue=2, maxvalue=8)
    out_h = int(in_h * scale)
    out_w = int(in_w * scale)
    out_image = []
    out_image = malloc(out_h, out_w, 200)

    for i in range(out_h):
        for k in range(out_w):
            # 실수위치 및 정수위치
            rh = i / scale
            rw = k / scale
            ih = int(rh)
            iw = int(rw)
            # 실수와 정수의 차이값
            x = rw - iw
            y = rh - ih

            if 0 <= ih < in_h - 1 and 0 <= iw < in_w - 1:
                # 결정할 위치(N)의 상하좌우 픽셀
                c1 = in_image[ih][iw]
                c2 = in_image[ih][iw + 1]
                c3 = in_image[ih + 1][iw + 1]
                c4 = in_image[ih + 1][iw]
                new_value = c1 *(1-y)*(1-x) + c2*(1-y)*x + c3*y*x + c4*y*(1-x)
                out_image[i][k] = int(new_value)

    display_image()


# zoom-out
def zoom_out_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_out', '(2~16)', minvalue=2, maxvalue=16)
    out_h = in_h // scale
    out_w = in_w // scale
    out_image = []
    out_image = malloc(out_h, out_w, 127)

    for i in range(out_h):
        for k in range(out_w):
            out_image[i][k] = in_image[i * scale][k * scale]

    display_image()


# zoom-in
def zoom_in_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_in', '(2~8)', minvalue=2, maxvalue=8)
    out_h = in_h * scale
    out_w = in_w * scale
    out_image = []
    out_image = malloc(out_h, out_w)
    for i in range(out_h):
        for k in range(out_w):
            out_image[i][k] = in_image[i // scale][k // scale]

    display_image()


# rotate
def rotate_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    angle = tkinter.simpledialog.askinteger(
        'rotate', '(1~360)', minvalue=1, maxvalue=360)
    radian = angle * math.pi / 180
    cx = in_w // 2
    cy = in_h // 2
    for i in range(in_h):
        for k in range(in_w):
            xs = i
            ys = k
            xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy)) + cx
            yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy)) + cy
            if 0 <= xd < out_h and 0 <= yd < out_w:
                out_image[xs][ys] = in_image[xd][yd]
            else:
                out_image[xs][ys] = 255

    display_image()


# histogram
def histogram_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    incountlist = [0] * 256
    outcountlist = [0] * 256

    for i in range(in_h):
        for k in range(in_w):
            incountlist[in_image[i][k]] += 1

    for i in range(out_h):
        for k in range(out_w):
            outcountlist[out_image[i][k]] += 1

    plt.plot(incountlist)
    plt.plot(outcountlist)
    plt.show()


# stretch
def stretch_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = []
    out_image = malloc(out_h, out_w)
    max_val = min_val = in_image[0][0]
    for i in range(in_h):
        for k in range(in_w):
            if in_image[i][k] < min_val:
                min_val = in_image[i][k]
            elif in_image[i][k] > max_val:
                max_val = in_image[i][k]
    for i in range(in_h):
        for k in range(in_w):
            out_image[i][k] = int(((in_image[i][k] - min_val) / (max_val - min_val)) * 255)

    display_image()


# end_in
def end_in_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = []
    out_image = malloc(out_h, out_w)
    max_val = min_val = in_image[0][0]
    for i in range(in_h):
        for k in range(in_w):
            if in_image[i][k] < min_val:
                min_val = in_image[i][k]
            elif in_image[i][k] > max_val:
                max_val = in_image[i][k]

    min_add = tkinter.simpledialog.askinteger('min_add', '(0~255)', minvalue=0, maxvalue=255)
    max_add = tkinter.simpledialog.askinteger('max_add', '(0~255)', minvalue=0, maxvalue=255)

    min_val += min_add
    max_val -= max_add

    for i in range(in_h):
        for k in range(in_w):
            value = int(((in_image[i][k] - min_val) / (max_val - min_val)) * 255)
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            out_image[i][k] = value

    display_image()


# equalize
def equalize_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = []
    out_image = malloc(out_h, out_w)
    histo = [0] * 256
    sum_histo = [0] * 256
    normal_histo = [0] * 256
    # 히스토그램
    for i in range(in_h):
        for k in range(in_w):
            histo[in_image[i][k]] += 1
    # 누적히스토그램
    s_value = 0
    for i in range(len(histo)):
        s_value += histo[i]
        sum_histo[i] = s_value
    # 정규화 누적 히스토그램
    for i in range(len(sum_histo)):
        normal_histo[i] = int(sum_histo[i] / (in_w * in_h) * 255)
    # 영상처리
    for i in range(in_h):
        for k in range(in_w):
            out_image[i][k] = normal_histo[in_image[i][k]]

    display_image()


# ========== Vision Algorithm(0.02) Endline ==========
# ========== Vision Algorithm(0.03) ==========
# mask processing
def mask_image(mask_number):
    global in_h, in_w, out_h, out_w, in_image, out_image
    global mask_list
    out_h = in_h
    out_w = in_w
    out_image = []
    out_image = malloc(out_h, out_w)
    m_size = 3
    mask = mask_list[mask_number]

    # 임시 입력영상 메모리 확보
    tmp_in_image = malloc(in_h + m_size - 1, in_w + m_size - 1, 127)
    tmp_out_image = malloc(out_h, out_w)

    # 원 입력 -> 임시 입력
    for i in range(in_h):
        for k in range(in_w):
            tmp_in_image[i + m_size // 2][k + m_size // 2] = in_image[i][k]

    # 회선연산
    for i in range(m_size // 2, in_h + m_size // 2):
        for k in range(m_size // 2, in_w + m_size // 2):
            # 각 점을 처리
            s = 0.0
            for m in range(0, m_size):
                for n in range(0, m_size):
                    s += mask[m][n] * tmp_in_image[i + m - m_size // 2][k + n - m_size // 2]
            tmp_out_image[i - m_size // 2][k - m_size // 2] = int(s)

    # 127 더하기
    if mask_number == 0:
        for i in range(out_h):
            for k in range(out_w):
                tmp_out_image[i][k] += 127

    # 임시 출력 -> 원 출력
    for i in range(out_h):
        for k in range(out_w):
            value = tmp_out_image[i][k]
            if value > 255:
                value = 255
            elif value < 0:
                value = 0
            out_image[i][k] = int(value)

    display_image()


# ========== Vision Algorithm(0.03) Endline ==========
# ========== Vision Algorithm(0.04) ==========
# morphing image
def morph_image():
    global window, canvas, paper, file_name, in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = []
    out_image = malloc(out_h, out_w)
    # 추가 영상 선택
    file_name2 = tk.filedialog.askopenfilename(
        parent=window,
        filetypes=(("RAW file", "*.raw"), ("All file", "*.*")),
    )
    if not is_open_file(file_name2):
        return

    fsize = os.path.getsize(file_name2)  # 파일의 크기(바이트)
    in_h2 = in_w2 = int(math.sqrt(fsize))  # 핵심 코드

    # 입력영상 메모리 확보
    in_image2 = []
    in_image2 = malloc(in_h2, in_w2)

    # 파일 --> 메모리
    with open(file_name2, 'rb') as rFp:
        for i in range(in_h2):
            for k in range(in_w2):
                in_image2[i][k] = int(ord(rFp.read(1)))

    def morp_func():
        w1 = 1
        w2 = 0
        for _ in range(20):
            for x in range(in_h):
                for y in range(in_w):
                    new_value = int(in_image[x][y] * w1 + in_image2[x][y] * w2)
                    if new_value > 255:
                        new_value = 255
                    elif new_value < 0:
                        new_value = 0
                    out_image[x][y] = new_value
            display_image()
            w1 -= 0.05
            w2 += 0.05
            time.sleep(0.5)

    threading.Thread(target=morp_func).start()


# ========== Vision Algorithm(0.04) Endline ==========
# ========== Vision Algorithm(0.05) ==========
# histogram custom
def histogram_image_custom():
    global in_h, in_w, out_h, out_w, in_image, out_image
    outcountlist = [0] * 256
    normalcountlist = [0] * 256

    # 빈도수 계산
    for i in range(out_h):
        for k in range(out_w):
            outcountlist[out_image[i][k]] += 1
    max_val = max(outcountlist)
    min_val = min(outcountlist)
    high = 256

    # 정규화 (카운트 값 - 최솟값) * high / (최댓값 - 최솟값)
    for i in range(len(outcountlist)):
        normalcountlist[i] = int((outcountlist[i] - min_val) * high / (max_val - min_val))

    # 서브 윈도우에 만들기
    sub_window = tk.Toplevel(window)
    sub_window.geometry('256x256')
    sub_canvas = tk.Canvas(sub_window, width=256, height=256)
    sub_paper = tk.PhotoImage(width=256, height=256)
    sub_canvas.create_image((256 // 2, 256 // 2), image=sub_paper, state='normal')

    # 서브 윈도우 출력
    for i in range(len(normalcountlist)):
        for k in range(int(normalcountlist[i])):
            data = 0
            sub_paper.put('#{:02x}{:02x}{:02x}'.format(data, data, data), (i, 255 - k))
    sub_canvas.pack(expand=1, anchor=tk.CENTER)
    sub_window.mainloop()


# ========== Vision Algorithm(0.05) Endline ==========
# ========== Vision Algorithm(0.06) ==========
def save_temp_image():
    global out_h, out_w, out_image, raw_file_list
    save_fp = f'{tempfile.gettempdir()}/{str(random.randint(10000, 99999))}.raw'
    if not is_open_file(save_fp):
        return

    with open(save_fp, mode='wb') as sf:
        for i in range(out_h):
            for j in range(out_w):
                sf.write(struct.pack('B', out_image[i][j]))

    return save_fp


# Get avg, max, min
def find_state(full_name, height, width):
    image = malloc(height, width)
    with open(full_name, 'rb') as rfp:
        for i in range(height):
            for j in range(width):
                image[i][j] = int(ord(rfp.read(1)))

    sum_val = 0
    max_val = min_val = image[0][0]
    for i in range(height):
        for j in range(width):
            value = image[i][j]
            if min_val > value:
                min_val = value
            if max_val < value:
                max_val = value
            sum_val += value

    avg = sum_val // (height * width)

    return avg, max_val, min_val


def upload_mysql():
    global raw_file_list

    if len(in_image) == 0:
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
            'raw_fname, raw_extname, raw_update, raw_uploader, '
            'raw_avg, raw_max, raw_min, raw_data) '
            f'VALUES(NULL, {str(height)}, {str(width)}, "{fname}", "{extname}",'
            f' "{up_date}", "{up_user}", {avg}, {max_val}, {min_val}, %s);'
            )

        # 서버로 보내기
        cur.execute(sql, (bin_data,))
        con.commit()

    # 서버 종료
    cur.close()
    con.close()


# download from mysql
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

        sql2 = ('SELECT raw_fname, raw_extname, raw_data '
                f'FROM rawimage_tbl WHERE raw_id = {str(raw_id)}')
        cur.execute(sql2)

        f_name, ext_name, bin_data = cur.fetchone()
        full_path = f'{tempfile.gettempdir()}/{f_name}.{ext_name}'

        with open(full_path, 'wb') as wfp:
            wfp.write(bin_data)

        cur.close()
        con.close()

        load_image(full_path)
        equal_image()
        display_image()

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
def save_as_csv():
    global window, out_image, out_h, out_w
    if len(out_image) == 0:
        tkinter.messagebox.showinfo(
            title='Error',
            message='Please open image frist',
        )
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window,
        filetypes=(('CSV file', '*.csv'), ('All file', '*.*')),
    )
    if save_fp == '' or save_fp is None:
        return

    with open(save_fp.name, 'w', newline='') as wfp:
        csv_writer = csv.writer(wfp)
        for i in range(out_h):
            for j in range(out_w):
                row_list = [i, j, out_image[i][j]]
                csv_writer.writerow(row_list)


def open_csv():
    global window, file_name
    file_name = tkinter.filedialog.askopenfilename(
        parent=window,
        filetypes=(('CSV file', '*.csv'), ('All file', '*.*')),
    )
    if not is_open_file(file_name):
        return

    load_csv(file_name)
    equal_image()
    display_image()


def load_csv(f_name):
    global in_h, in_w, in_image
    f_size = 0
    with open(f_name, 'r') as rfp:
        for _ in rfp:
            f_size += 1
    in_h = in_w = int(math.sqrt(f_size))
    in_image = malloc(in_h, in_w)

    with open(f_name, 'r') as rfp:
        for row_list in rfp:
            col, row, value = map(int, row_list.strip().split(','))
            in_image[col][row] = value


# ========== Vision Algorithm(0.07) Endline ==========
# ========== Vision Algorithm(0.08) ==========
# save as excel
def save_as_excel():
    global window, out_image, out_h, out_w
    if len(out_image) == 0:
        tkinter.messagebox.showinfo(title='Error',
                                    message='Please open image frist')
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window,
        mode='wb',
        defaultextension='*.xls',
        filetypes=(('EXCEL file', '*.xls'), ('All file', '*.*')),
    )

    if save_fp == '' or save_fp is None:
        return

    xls_name = save_fp.name
    sheet_name = os.path.basename(xls_name)
    workbook = xlsxwriter.Workbook(xls_name)
    worksheet = workbook.add_worksheet(sheet_name)

    for i in range(out_h):
        for j in range(out_w):
            worksheet.write(i, j, out_image[i][j])

    workbook.close()


# save as excel art
def save_as_excel_art():
    global window, out_image, out_h, out_w
    if len(out_image) == 0:
        tkinter.messagebox.showinfo(title='Error',
                                    message='Please open image frist')
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window,
        mode='wb',
        defaultextension='*.xls',
        filetypes=(('EXCEL file', '*.xls'), ('All file', '*.*')),
    )
    xls_name = save_fp.name
    sheet_name = os.path.basename(xls_name)
    workbook = xlsxwriter.Workbook(xls_name)
    worksheet = workbook.add_worksheet(sheet_name)

    # 행과 열을 정사각형으로 만들기
    # 열 길이 수정
    worksheet.set_column(0, out_h - 1, 1.0)
    # 행 길이 수정
    for i in range(out_h):
        worksheet.set_row(i, 9.5)

    # 셀에 값을 채워 넣기
    for i in range(out_h):
        for j in range(out_w):
            data = out_image[i][j]
            # data 값으로 셀의 배경색을 조절 #000000 ~ #FFFFFF
            if data > 15:
                hex_str = f'#{hex(data)[2:] * 3}'
            else:
                hex_str = f'#{("0" + hex(data)[2:]) * 3}'
            # sell format
            cell_format = workbook.add_format()
            cell_format.set_bg_color(hex_str)
            worksheet.write(i, j, '', cell_format)

    workbook.close()


# open excel
def open_excel():
    global window, file_name
    file_name = tkinter.filedialog.askopenfilename(
        parent=window,
        filetypes=(('EXCEL file', '*.xls;*.xlsx'), ('All file', '*.*')),
    )
    if file_name == '' or file_name is None:
        return

    load_excel(file_name)
    equal_image()
    display_image()


# load excel
def load_excel(f_name):
    global in_h, in_w, in_image
    workbook = xlrd.open_workbook(f_name)
    worksheet = workbook.sheet_by_index(0)
    in_w = worksheet.ncols
    in_h = worksheet.nrows
    in_image = []
    in_image = malloc(in_h, in_w)

    for i in range(in_h):
        for j in range(in_w):
            in_image[i][j] = int(worksheet.cell_value(i, j))


# ========== Vision Algorithm(0.08) Endline ==========
# ==================== Main code ====================
if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    window.title('Computer Vision (Ver 0.09)')

    status = tk.Label(window, text='Please open file', bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)

    canvas = tk.Canvas(window, height=512, width=512, bg='white')
    canvas.pack(expand=1, anchor=tk.CENTER)

    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    file_menu = tk.Menu(main_menu)
    main_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Open RAW file', command=open_image)
    file_menu.add_separator()
    file_menu.add_command(label='Save file', command=save_image)

    comvision_menu1 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Pixel', menu=comvision_menu1)
    comvision_menu1.add_command(label='Brighten/Darken', command=add_image)
    comvision_menu1.add_command(label='Invert', command=invert_image)
    comvision_menu1.add_command(label='Parabola', command=para_image)
    comvision_menu1.add_separator()
    comvision_menu1.add_command(label="Morphing_image", command=morph_image)

    comvision_menu2 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Statistics', menu=comvision_menu2)
    comvision_menu2.add_command(label='Black&White', command=bw_image)
    comvision_menu2.add_command(label='Zoom_out(better)', command=zoom_out_image2)
    comvision_menu2.add_command(label='Zoom_in(better)', command=zoom_in_image2)
    comvision_menu2.add_separator()
    comvision_menu2.add_command(label='Histogram', command=histogram_image)
    comvision_menu2.add_command(label='Histogram_custom', command=histogram_image_custom)
    comvision_menu2.add_command(label='Stretch', command=stretch_image)
    comvision_menu2.add_command(label='End_In', command=end_in_image)
    comvision_menu2.add_command(label='Equalize', command=equalize_image)

    comvision_menu3 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Geometry', menu=comvision_menu3)
    comvision_menu3.add_command(label='Up_Down', command=up_down_image)
    comvision_menu3.add_command(label='Move', command=move_image)
    comvision_menu3.add_command(label='Zoom_out', command=zoom_out_image)
    comvision_menu3.add_command(label='Zoom_in', command=zoom_in_image)
    comvision_menu3.add_command(label='Rotate', command=rotate_image)

    comvision_menu4 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Area', menu=comvision_menu4)
    comvision_menu4.add_command(label='Embossing', command=lambda: mask_image(0))
    comvision_menu4.add_command(label='Blurring', command=lambda: mask_image(1))
    comvision_menu4.add_command(label='Sharpening', command=lambda: mask_image(2))
    comvision_menu4.add_command(label='Edge detect', command=lambda: mask_image(3))
    comvision_menu4.add_command(label='Gaussian', command=lambda: mask_image(4))
    comvision_menu4.add_command(label='High freq', command=lambda: mask_image(5))
    comvision_menu4.add_command(label='Low freq', command=lambda: mask_image(6))

    comvision_menu5 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Format', menu=comvision_menu5)
    comvision_menu5.add_command(label='Upload in MySQL', command=upload_mysql)
    comvision_menu5.add_command(label='Download from MySQL', command=download_mysql)
    comvision_menu5.add_separator()
    comvision_menu5.add_command(label='Save as CSV file', command=save_as_csv)
    comvision_menu5.add_command(label='Open CSV file', command=open_csv)
    comvision_menu5.add_separator()
    comvision_menu5.add_command(label='Save as Excel file', command=save_as_excel)
    comvision_menu5.add_command(label='Save as Excel Art', command=save_as_excel_art)
    comvision_menu5.add_command(label='Open Excel file', command=open_excel)

    open_image()
    window.mainloop()
