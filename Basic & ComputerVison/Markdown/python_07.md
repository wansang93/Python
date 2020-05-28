# 07일차 파이썬 데이터 시각화 190613

## 과제풀이 및 코드

### 흑백 이미지(.raw) 시각화 알고리즘

- Geometry
  - Up-down : 뒤집기
  - Move(with Mouse) : 마우스로 움직이기
  - Zoom-Out : 축소하기(일반, 평균변환)
  - Zoom-In : 확대하기(일반, 양선형보간법)
  - Rotate : 회전
- Pixel
  - Histogram : 각 픽셀의 분포를 보여줌
  - Stretch : 이상적이지 못한 히스토그램 분포 중에서 명암 대비가 낮은 디지털 영상의 품질을 향상 시키는 기술
  
    new pixel = (old pixel-low)/(high-low)*255
  
  - End-In : 일정한 양의 화소를 흰색이나 검정으로 지정하여 히스토그램의 분포를 좀 더 균일하게 만듬
  
    new pixel = 0 if old pixel <= low
  
    new pixel = 255 if old pixel >= high
  
    new pixel = (old pixel-low)/high-low*255 if low <= old pixel <= high
  
  - Equalize : 어두운 영상의 히스토그램을 조절하여 명암 분포가 빈약한 영상을 균일하게 만들어 줌, 영상의 밝기 분포를 재분배하여 명암 대비를 최대화, 명암 대비를 자동으로 조정, 명암의 빈도는 변경하지않음, 검출 특성을 증가시킴
  
    1단계 : 명암 값 j의 빈도 수 hist[j]를 계산해 입력 영상의 히스토그램 생성
  
    2단계 : 각 명암 값 i에서 0~i까지의 누적 빈도 수(누적합)를 계산
  
    3단계 : 2단계에서 구한 누적 빈도 수를 정규화
- Area
  
  - embossing : 마스크를 씌워 이미지의 값을 변경

### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.02

- 코드 07-01, 02, 03, 04

``` python
import matplotlib.pyplot as plt
```

``` python
# ==================== Global Variable ====================
# ========== Mouse Event ==========
panYN = False
sx, sy, ex, ey = [0] * 4
```

- def display_image(): move 기능 추가, 성능 개선 추가

``` python
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
``` 

``` python
# ==================== Function Declaration ====================
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
```

``` python
# ==================== Main code ====================
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
```

## 과제

- 회전 수정
- 마스크 추가
- 엠보싱, 블러링, 샤프닝, 경계선 검출, 가우시안 필터링, 고주파, 저주파

### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.03

- def malloc() 수정

``` python
def malloc(h, w, init_value=0):
    reg_memory = []
    for _ in range(h):
        tem_list = []
        for _ in range(w):
            tem_list.append(init_value)
        reg_memory.append(tem_list)
    return reg_memory
```

- def save_image() 수정 및 라이브러리에 struct 추가

``` python
import struct

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
```

``` python
# ==================== Global Variable ====================
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
```

``` python
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
```

``` python
# ==================== Main code ====================
    comVisionMenu4 = tk.Menu(mainMenu)
    mainMenu.add_cascade(label='Area', menu=comVisionMenu4)
    comVisionMenu4.add_command(label='embossing', command=lambda: mask_image(0))
    comVisionMenu4.add_command(label='blurring', command=lambda: mask_image(1))
    comVisionMenu4.add_command(label='sharpening', command=lambda: mask_image(2))
    comVisionMenu4.add_command(label='edge detect', command=lambda: mask_image(3))
    comVisionMenu4.add_command(label='gaussian', command=lambda: mask_image(4))
    comVisionMenu4.add_command(label='high freq', command=lambda: mask_image(5))
    comVisionMenu4.add_command(label='low freq', command=lambda: mask_image(6))
```