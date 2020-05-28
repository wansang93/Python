import tkinter as tk
import tkinter.simpledialog
import tkinter.filedialog
import os
import math


# ==================== Global Variable ====================
window, canvas, paper = None, None, None
inH, inW, outH, outW = [0] * 4
inImage, outImage = [], []
filename = ''


# ==================== Function Declaration ====================
# ========== file I/O ==========
# memory declaration
def malloc(h, w):
    reg_memory = []
    for _ in range(h):
        tem_list = []
        for _ in range(w):
            tem_list.append(0)
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
    pass

# display image
def display_image():
    global inH, inW, outH, outW, inImage, outImage, filename, window, canvas, paper
    if canvas is not None:
        canvas.destroy()

    canvas = tk.Canvas(window, height=512, width=512, relief='solid', bd=2, bg='white')
    paper = tk.PhotoImage(height=outH, width=outW)
    canvas.create_image((outH//2, outW//2), image=paper, state='normal', anchor=tk.CENTER)

    for i in range(outH):
        for k in range(outW):
            r = g = b = outImage[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

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

    
# ==================== Main code ====================
if __name__ == '__main__':

    window = tk.Tk()
    window.geometry('600x600')
    window.title('Computer Vision (Ver 0.01)')

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

    open_image()
    window.mainloop()
