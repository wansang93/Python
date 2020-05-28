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
    with open(filename, 'rb') as rFp:
        for i in range(inH):
            for k in range(inW):
                inImage[i][k] = int(ord(rFp.read(1)))  # ord()는 아스키 값을 읽는 함수, 반대는 chr()이다.

# open image
def open_image():
    global inH, inW, outH, outW, inImage, outImage, filename
    filename = tkinter.filedialog.askopenfilename(
        parent=window, filetype=(('RAW file', '*.raw'), ('All file', '*.*')))
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
    if canvas is not None:
        canvas.destroy()

    canvas = tk.Canvas(window, height=512, width=512, relief='solid', bd=0, bg='white')
    paper = tk.PhotoImage(height=outH, width=outW)
    canvas.create_image((outH//2, outW//2), image=paper, state='normal', anchor=tk.CENTER)

    # for i in range(outH):
    #     for k in range(outW):
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    # 성능 개선
    rgb_str = ''
    for i in range(outH):
        tmp_str = ''
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmp_str += ' #{:02x}{:02x}{:02x}'.format(r, g, b)
        rgb_str += '{{{}}} '.format(tmp_str)
    paper.put(rgb_str)

    canvas.bind('<Button-1>', mouse_click)
    canvas.bind('<ButtonRelease-1>', mouse_drop)
    canvas.pack(expand=1, anchor=tk.CENTER)

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
    
# ==================== Main code ====================
if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('600x600')
    window.title('Computer Vision (Ver 0.03)')

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

    comVisionMenu2 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Geometry', menu=comVisionMenu2)
    comVisionMenu2.add_command(label='Black&White', command=bw_image)
    comVisionMenu2.add_command(label='zoom_out(better)', command=zoom_out_image2)
    comVisionMenu2.add_command(label='zoom_in(better)', command=zoom_in_image2)
    comVisionMenu2.add_separator()
    comVisionMenu2.add_command(label='Histogram', command=histogram_image)
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

    open_image()
    window.mainloop()
