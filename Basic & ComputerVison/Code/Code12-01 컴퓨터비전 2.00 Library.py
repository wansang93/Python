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
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import pymysql
import xlrd
import xlsxwriter


# ==================== Global Variable ====================
window, canvas1, canvas2, paper1, paper2 = [None] * 5
in_h, in_w, in_image = 0, 0, []
out_h, out_w, out_image = 0, 0, []
file_name = ''
VIEW_X, VIEW_Y = 512, 512
R, G, B = 0, 1, 2
# ========== Mouse Event ==========
pan_yn = False
sx, sy, ex, ey = [0] * 4
# ========== Mask Value ==========
# size, scale, offset, kernel
# embossing mask(0)
embossing = (3, 3), 1, 128, (
    -1, 0, 0,
    0, 0, 0,
    0, 0, 1
)
# blurring mask(1)
blurring = (3, 3), 9, 0, (
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
)
# sharpening mask(2)
sharpening = (3, 3), 1, 0, (
    0, -1, 0,
    -1, 5, -1,
    0, -1, 0
)
# edge detect mask(3)
edge_detect = (3, 3), 1, 0, (
    0, 0, 0,
    -1, 1, 0,
    0, 0, 0
)
# gaussian mask(4)
gaussian = (3, 3), 1, 0, (
    1/16, 1/8, 1/16,
    1/8, 1/4, 1/8,
    1/16, 1/8, 1/16
)
# high frequency(5)
high_freq = (3, 3), 9, 0, (
    -1, -1, -1,
    -1, 8, -1,
    -1, -1, -1
)
# low frequency(6)
low_freq = (3, 3), 9, 0, (
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
)
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
    if out_image is None:
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
    file_name = 'D:/☆☆☆멀캠생활/Image/Pet_PNG(512x512)/cat01_512.png'
    # file_name = tkinter.filedialog.askopenfilename(
    #     parent=window,
    #     filetypes=(('Color file', '*.jpg;*.png;*.bmp;*.gif;*.tif'), ('All file', '*.*')),
    # )
    if not is_open_file(file_name):
        return

    load_image(file_name)
    equal_image()
    display_new_image()


# load image
def load_image(file_name):
    global in_h, in_w, in_image
    in_image = Image.open(file_name)
    in_h = in_image.height
    in_w = in_image.width


# display new image
def display_new_image():
    global window, canvas1, canvas2, paper1, paper2, file_name
    global in_h, in_w, in_image
    global VIEW_X, VIEW_Y
    if canvas1:
        canvas1.destroy()
    if canvas2:
        canvas2.destroy()

    canvas1 = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, bg='white')
    paper1 = tk.PhotoImage(height=in_h, width=in_w)
    canvas1.create_image((in_h//2, in_w//2), image=paper1, anchor=tk.CENTER)
    canvas2 = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, relief='solid', bd=2, bg='white')
    canvas1.pack(expand=1, side=tk.LEFT)
    canvas2.pack(expand=1, side=tk.RIGHT)

    step_x, step_y = 1, 1
    if in_h > VIEW_Y:
        step_y = in_h / VIEW_Y
    if in_w > VIEW_X:
        step_x = in_w / VIEW_X

    rgb_str = ''
    rgb_image = in_image.convert('RGB')
    for i in np.arange(0, in_h, step_y):
        i = int(i)
        tmp_str = ''
        for j in np.arange(0, in_w, step_x):
            j = int(j)
            r, g, b = rgb_image.getpixel((j, i))
            tmp_str += f' #{r:02x}{g:02x}{b:02x}'
        rgb_str += f'{{{tmp_str}}} '
    paper1.put(rgb_str)
    status.configure(text=f'Image is opened from ({file_name}) {in_h}x{in_w}')


# display out image
def display_out_image():
    global window, canvas2, paper2, file_name
    global in_h, in_w, in_image, out_h, out_w, out_image
    global VIEW_X, VIEW_Y
    if canvas2:
        canvas2.destroy()

    canvas2 = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, bg='white')
    paper2 = tk.PhotoImage(height=out_h, width=out_w)
    canvas2.create_image((out_h//2, out_w//2), image=paper2, anchor=tk.CENTER)
    
    step_x, step_y = 1, 1
    if out_h > VIEW_Y:
        step_y = out_h / VIEW_Y
    if out_w > VIEW_X:
        step_x = out_w / VIEW_X

    rgb_str = ''
    rgb_image = out_image.convert('RGB')
    for i in np.arange(0, out_h, step_y):
        i = int(i)
        tmp_str = ''
        for j in np.arange(0, out_w, step_x):
            j = int(j)
            r, g, b = rgb_image.getpixel((j, i))
            tmp_str += f' #{r:02x}{g:02x}{b:02x}'
        rgb_str += f'{{{tmp_str}}} '
    paper2.put(rgb_str)

    canvas2.bind('<Button-1>', mouse_click)
    canvas2.bind('<ButtonRelease-1>', mouse_drop)
    canvas2.pack(expand=1, side=tk.RIGHT)

    status.configure(
        text=(f'Image is opened from ({file_name}) '
            f'{in_h}x{in_w}, Out image is printed {out_h}x{out_w}')
    )


# save image
def save_out_image():
    global out_h, out_w, out_image, window
    if is_empty_image():
        return

    save_fp = tkinter.filedialog.asksaveasfile(
        parent=window,
        mode='wb',
        defaultextension='*.jpg',
        filetypes=(('JPG file', '*.jpg'), ('All file', '*.*')),
    )
    if not is_save_file(save_fp):
        return

    status.configure(text=f'Image is being saved at {save_fp.name}')
    out_image.save(save_fp.name)
    status.configure(text=f'Image is saved at {save_fp.name}')
    save_fp.close()


# ========== Vision Algorithm(2.00) ==========
# equal image
def equal_image():
    global in_h, in_w, out_h, out_w, in_image, out_image
    out_h = in_h
    out_w = in_w
    out_image = in_image.copy()


# bright control(*)
def multiply_image():
    global in_image, out_image
    if is_empty_image():
        return
    equal_image()
    
    value = tkinter.simpledialog.askfloat(
        'bright *',
        'multiply float(0~16)',
        minvalue=0.0,
        maxvalue=16.0,
    )
    out_image = in_image.copy()
    out_image = ImageEnhance.Brightness(out_image).enhance(value)

    display_out_image()


# invert image
def invert_image():
    global in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = ImageOps.invert(in_image)

    display_out_image()


# parabola image
def para_image():
    global in_image, out_image
    if is_empty_image():
        return
    equal_image()

    fn = lambda x: int(255 - 255 * math.pow(x / 128 - 1, 2))
    out_image = in_image.point(fn)

    display_out_image()


# black & white image
def bw_image():
    global in_image, out_image
    if is_empty_image():
        return
    equal_image()

    fn = lambda x: 255 if x >= 127 else 0
    out_image = in_image.convert('L').point(fn)

    display_out_image()


# ========== Vision Algorithm(2.00) ==========
# Move Display
def move_image():
    global pan_yn, canvas2
    if is_empty_image():
        return
    equal_image()

    display_out_image()
    pan_yn = True
    canvas2.configure(cursor='mouse')


def mouse_click(event):
    global sx, sy, ex, ey, pan_yn
    if not pan_yn:
        return
    sx = event.x
    sy = event.y


def mouse_drop(event):
    global in_h, in_w, in_image, out_image
    global sx, sy, ex, ey, pan_yn
    if not pan_yn:
        return
    mx = event.x - sx
    my = event.y - sy
    out_image = ImageChops.offset(in_image, mx, my)
    pan_yn = False

    display_out_image()


# upside-down
def up_down_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.transpose(Image.FLIP_TOP_BOTTOM)

    display_out_image()


# zoom-out(better)
def zoom_out_image2():
    global in_h, in_w, in_image, out_h, out_w, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_out', '(2~16)', minvalue=2, maxvalue=16)

    out_image = out_image.resize(
        (in_h//scale, in_w//scale),
        resample=Image.BICUBIC
    )
    out_h = out_image.height
    out_w = out_image.width

    display_out_image()
    out_h = in_h
    out_w = in_w


# zoom-in(better)
def zoom_in_image2():
    global in_h, in_w, in_image, out_h, out_w, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_in', '(2~16)', minvalue=2, maxvalue=16)
    
    out_image = out_image.resize(
        (in_h*scale, in_w*scale),
        resample=Image.LANCZOS
    )
    out_h = out_image.height
    out_w = out_image.width

    display_out_image()
    out_h = in_h
    out_w = in_w

# zoom-out
def zoom_out_image():
    global in_h, in_w, in_image, out_h, out_w, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_out', '(2~16)', minvalue=2, maxvalue=16)

    out_image = out_image.resize((in_h//scale, in_w//scale))
    out_h = out_image.height
    out_w = out_image.width

    display_out_image()
    out_h = in_h
    out_w = in_w


# zoom-in
def zoom_in_image():
    global in_h, in_w, in_image, out_h, out_w, out_image
    if is_empty_image():
        return
    equal_image()

    scale = tkinter.simpledialog.askinteger(
        'zoom_in', '(2~16)', minvalue=2, maxvalue=16)

    out_image = out_image.resize((in_h*scale, in_w*scale))
    out_h = out_image.height
    out_w = out_image.width

    display_out_image()
    out_h = in_h
    out_w = in_w


# rotate
def rotate_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    angle = tkinter.simpledialog.askinteger(
        'rotate', '(1~360)', minvalue=1, maxvalue=360)
    white = (255, 255, 255)
    out_image = in_image.rotate(angle, fillcolor=white)
    out_h = out_image.height
    out_w = out_image.width

    display_out_image()



# histogram
def histogram_image():
    if is_empty_image():
        return

    in_r, in_g, in_b = in_image.split()

    plt.plot(in_r.histogram(), color='r')
    plt.plot(in_g.histogram(), color='g')
    plt.plot(in_b.histogram(), color='b')
    plt.show()


# TODO: stretch, end_in, equalize
# stretch
def stretch_image():
    pass
# end_in
def end_in_image():
    pass
# equalize
def equalize_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = ImageOps.equalize(in_image)

    display_out_image()

# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# mask processing
def mask_image(mask_number=0):
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    size, scale, offset, kernel = mask_list[mask_number]
    k = ImageFilter.Kernel(
        size=size,
        scale=scale,
        offset=offset,
        kernel=kernel
    )

    out_image = in_image.filter(k)

    display_out_image()


# embossing
def embossing_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.EMBOSS)

    display_out_image()


# blurring
def blurring_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.BLUR)

    display_out_image()


# sharpening
def sharpening_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.SHARPEN)

    display_out_image()


# edge_detect
def edge_detect_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.FIND_EDGES)

    display_out_image()


# gaussian
def gaussian_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.GaussianBlur)

    display_out_image()


# high_freq
def high_freq_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.EDGE_ENHANCE)

    display_out_image()


# low_freq
def low_freq_image():
    global out_h, out_w, in_image, out_image
    if is_empty_image():
        return
    equal_image()

    out_image = in_image.filter(ImageFilter.EDGE_ENHANCE_MORE)

    display_out_image()


# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# morphing image
def morph_image():
    pass
# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# histogram custom
def histogram_image_custom():
    pass
# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# save image at temp
def save_out_image_at_temp():
    pass
# Get avg, max, min
def find_state():
    pass
# upload to mysql
def upload_mysql():
    pass
# download from mysql
def download_mysql():
    pass
# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# save as csv
def save_as_csv():
    pass
# open csv
def open_csv():
    pass
# load csv
def load_csv(file_name):
    pass
# ========== Vision Algorithm(2.00) Endline ==========
# ========== Vision Algorithm(2.00) ==========
# save as excel
def save_as_excel():
    pass
# save as excel art
def save_as_excel_art():
    pass
# open excel
def open_excel():
    pass
# load excel
def load_excel(file_name):
    pass
# ========== Vision Algorithm(2.00) Endline ==========

# ==================== Main code ====================
if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('1100x600')
    window.title('Computer Vision Color(Ver 2.00)')

    status = tk.Label(window, text='Please open a image file', bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)

    canvas1 = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, relief='solid', bd=2, bg='white')
    canvas1.pack(side=tk.LEFT)
    canvas2 = tk.Canvas(window, height=VIEW_Y, width=VIEW_X, relief='solid', bd=2, bg='white')
    canvas2.pack(side=tk.RIGHT)

    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    file_menu = tk.Menu(main_menu)
    main_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Open Color file', command=open_image)
    file_menu.add_separator()
    file_menu.add_command(label='Save file', command=save_out_image)

    comvision_menu1 = tk.Menu(main_menu)
    main_menu.add_cascade(label='Pixel', menu=comvision_menu1)
    comvision_menu1.add_command(label='Brighten/Darken', command=multiply_image)
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
    comvision_menu4.add_command(label='Library Embossing', command=embossing_image)
    comvision_menu4.add_command(label='Library Blurring', command=blurring_image)
    comvision_menu4.add_command(label='Library Sharpening', command=sharpening_image)
    comvision_menu4.add_command(label='Library Edge detect', command=edge_detect_image)
    comvision_menu4.add_command(label='Library Gaussian', command=gaussian_image)
    comvision_menu4.add_command(label='Library High freq', command=high_freq_image)
    comvision_menu4.add_command(label='Library Low freq', command=low_freq_image)

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
