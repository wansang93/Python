# 11일차 파이썬 총 복습 및 리뷰 190619

오늘은 지금까지 한 파이썬 총 복습 및 리뷰의 시간이였습니다.

자세한 필기는 다음 링크 참고 -> [https://github.com/RYUNSUN/](https://github.com/RYUNSUN/AI_Curriculum_Multicampus/blob/master/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0(%EB%94%A5%EB%9F%AC%EB%8B%9D)%20%ED%99%9C%EC%9A%A9%20AI%20%EC%84%A4%EA%B3%84/%EB%94%A5%EB%9F%AC%EB%8B%9D%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B8%B0%EC%B4%88_Python/Contents/190619_day11.md)

## 복습 1~10일차

1. 컴퓨터 : 크게 H/W 와 S/W로 나누어짐
   - H/W : CPU(사람, 두뇌), RAM(작업대), Disk(책장)
     - CPU : Intel Core i-3, 5, 7, 9 + 1~9세대, 코어갯수(2, 4, 8, 16...)
     - RAM : 전원이 끊기면 다 날라감, 삼성, DDR4(8GB, 16GB...)
     - Disk : HDD(1TB, 2TB, 4TB...) 오래사용하면 깨질 수 있다, SSD - 안정성이 높다
     - Graphic Card : 내장(CPU) / 외장(Geoforce)
   - S/W : OS + App
     - OS : Unix, Linux, Windows, Mac
       - Unix : 주로 회사제품에 사용, IBM AIX, HP UX
       - Linux : Redhat Enterpise(RHEL), CentOS, Fedora(Beta), Oracle Unix 등
         - Redhat 계열 : 기업화 된 배포판 - RHEL, CentOS, Fedora, Oracle Unix
         - Debian 계열 : Ubuntu
       - Windows : Windows7, 10, Windows Server 2016, 2019...
       - Mac : Apple
2. 가상머신
   - Azure, VMware, Virtual Box
   - OS 설치 : Windows 2016, 2019, Linux
3.  DBMS
   - IBM : DB2
   - Oracle DB : 대규모 - 버전 10g, 11gR1/R2, 12cR1/R2, 18c
   - SQL Server : 중대규모 - 2008, 2008R2, 2012, 2014, 2016, 2017, 2019
   - MySQL : 중소규모 - 5.6, 5.7, 8.0
   - MariaDB : 오픈소스(무료) - 버전 10.1, 10.2, 10.3, 10.4(RC)
4. DBMS 구축 및 데이터 활용
   - DBMS설치-> DB생성 -> Table생성 -> 데이터 입력/수정/삭제
   - 2일차 : DB Server(MySQL)와 DB Client(HeidiSQL) 연동하여 조작
   - 3일차 : Python에서 pymysql이라는 외부 라이브러리를 사용하여 MySQL 조작

## 과제

1. 컴퓨터비전 가능한 부분은 NumPy 버전으로 변경

   ``` python
   import math
   import os
   import struct
   import tkinter.filedialog
   import tkinter.messagebox
   import tkinter.simpledialog
   import tkinter as tk

   import numpy as np


   # ==================== Global Variable ====================
   window, canvas1, canvas2, paper1, paper2 = [None] * 5
   file_name = ''
   in_h, in_w, in_image = 0, 0, []
   out_h, out_w, out_image = 0, 0, []
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
   # ========== Server default ==========
   IP_ADDR = '192.168.111.10'
   USER_NAME = 'root'
   USER_PW = '1234'
   DB_NAME = 'bigdata_db'
   CHAR_SET = 'utf8'
   raw_file_list = []


   # ==================== Function Declaration ====================
   # ========== Bug Check ==========
   def is_open_file(fname):
      if not fname:
         status.configure(text='Open is failed. Please try again')
         return True
      return False


   def is_save_file(fname):
      if not fname:
         status.configure(text=f'Save is failed. Please try again')
         return True
      return False


   def is_empty_image():
      global out_image
      if len(out_image) == 0:
         tkinter.messagebox.showinfo(title='Error',
               message='The image is empty, Please open image')
         return True
      return False

   # ========== file I/O ==========
   # memory allocation
   def malloc(h, w, initvalue=0, datatype=np.uint8):
      ret_memory = np.zeros((h, w), dtype=datatype)
      ret_memory += initvalue
      return ret_memory


   # open image
   def open_image():
      global window, file_name
      file_name = tkinter.filedialog.askopenfilename(
         parent=window,
         filetypes=(('RAW file', '*.raw'), ('All file', '*.*')),
      )
      if is_open_file(file_name):
         return

      load_image(file_name)
      equal_image()


   # load image
   def load_image(fname):
      global in_h, in_w, in_image
      fsize = os.path.getsize(fname)
      in_h = int(math.sqrt(fsize))
      in_w = int(math.sqrt(fsize))
      in_image = np.fromfile(fname, dtype=np.uint8)
      in_image = in_image.reshape(in_h, in_w)


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

      step_X, step_Y = 1, 1
      if in_h > VIEW_Y:
         step_Y = in_h / VIEW_Y
      if in_w > VIEW_X:
         step_X = in_w / VIEW_X

      rgb_str = ''
      for i in np.arange(0, in_h, step_Y):
         tmp_str = ''
         for j in np.arange(0, in_w, step_X):
               i = int(i)
               j = int(j)
               r = g = b = in_image[i][j]
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
      
      step_X, step_Y = 1, 1
      if out_h > VIEW_Y:
         step_Y = out_h / VIEW_Y
      if out_w > VIEW_X:
         step_X = out_w / VIEW_X

      rgb_str = ''
      for i in np.arange(0, out_h, step_Y):
         tmp_str = ''
         for j in np.arange(0, out_w, step_X):
               i = int(i)
               j = int(j)
               r = g = b = out_image[i][j]
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


   # equal image
   def equal_image():
      global in_h, in_w, out_h, out_w, in_image, out_image
      out_h = in_h
      out_w = in_w
      out_image = in_image.copy()

      display_new_image()


   # save image
   def save_out_image():
      global window, out_h, out_w, out_image
      if is_empty_image():
         return

      savefp = tkinter.filedialog.asksaveasfile(
         parent=window,
         mode='wb',
         defaultextension='*.raw',
         filetypes=(('RAW file', '*.raw'), ('All file', '*.*')),
      )
      if is_save_file(savefp):
         return

      status.configure(text=f'Image is being saved at {savefp.name}')
      for i in range(out_h):
         for j in range(out_w):
               savefp.write(struct.pack('B', out_image[i][j]))
      status.configure(text=f'Image is saved at {savefp.name}')
      savefp.close()


   # ========== Vision Algorithm(1.01) ==========
   # bright control(+/-)
   def add_image():
      global in_image, out_image
      if is_empty_image():
         return
      out_image = in_image

      value = tkinter.simpledialog.askinteger(
         'bright +/-',
         '(-255~255)',
         minvalue=-255,
         maxvalue=255,
      )
      out_image = out_image.astype(np.int16) + value
      out_image = np.where(out_image > 255, 255, out_image)
      out_image = np.where(out_image < 0, 0, out_image)
      display_out_image()


   # reverse image
   def rev_image():
      global in_image, out_image
      if is_empty_image():
         return
      out_image = in_image

      out_image = 255 - out_image
      display_out_image()


   # para image
   def para_image():
      global in_image, out_image
      if is_empty_image():
         return
      out_image = in_image

      x = np.array([i for i in range(256)])
      LUT = 255 - 255 * np.power(x / 128 -1, 2)
      LUT = LUT.astype(np.uint8)
      out_image = LUT[out_image]
      display_out_image()


   # bw image
   def bw_image():
      global in_image, out_image
      if is_empty_image():
         return
      out_image = in_image

      avg = np.average(out_image)
      out_image = np.where(out_image > avg, 255, 0)
      display_out_image()


   # ========== Vision Algorithm(1.02) ==========
   # Move Display
   def move_image():
      global panYN, canvas2
      panYN = True
      canvas2.configure(cursor='mouse')


   def mouse_click(event):
      global sx, sy, ex, ey, panYN
      if not panYN:
         return
      sx = event.x
      sy = event.y


   def mouse_drop(event):
      global in_h, in_w, in_image, out_image
      global sx, sy, ex, ey, panYN
      if not panYN:
         return
      out_image = malloc(in_h, in_w, 255)
      mx = event.x - sx
      my = event.y - sy
      if mx >= 0 and my >= 0:
         out_image[my:in_h, mx:in_w] = in_image[0:in_h-my, 0:in_w-mx]
      elif mx >= 0 and my <= 0:
         out_image[0:in_h+my, mx:in_w] = in_image[-1*(my):in_h, 0:in_w-mx]
      elif mx <= 0 and my >= 0:
         out_image[my:in_h, 0:in_w+mx] = in_image[0:in_h-my, -1*(mx):in_w]
      elif mx <= 0 and my <= 0:
         out_image[0:in_h+my, 0:in_w+mx] = in_image[-1*(my):in_h, -1*(mx):in_w]
      display_out_image()


   # upside-down
   def up_down_image():
      global in_image, out_image
      if is_empty_image():
         return
      out_image = in_image

      out_image = np.flip(in_image, axis=0)
      display_out_image()


   # zoom-out(평균변환)
   def zoom_out_image2():
      pass
   # zoom-in(양선형 보간)
   def zoom_in_image2():
      pass
   # zoom-out
   def zoom_out_image():
      pass
   # zoom-in
   def zoom_in_image():
      pass
   # rotate
   def rotate_image():
      pass
   # histogram
   def histogram_image():
      pass
   # stretch
   def stretch_image():
      pass
   # end_in
   def end_in_image():
      pass
   # equalize
   def equalize_image():
      pass
   # ========== Vision Algorithm(1.02) Endline ==========
   # ========== Vision Algorithm(1.03) ==========
   # Mask Processing
   def mask_image(num=0):
      pass
   # ========== Vision Algorithm(1.03) Endline ==========
   # ========== Vision Algorithm(1.04) ==========
   # morph image
   def morph_image():
      pass
   # ========== Vision Algorithm(1.04) Endline ==========
   # ========== Vision Algorithm(1.05) ==========
   # histogram_custom
   def histogram_image_custom():
      pass
   # ========== Vision Algorithm(1.05) Endline ==========
   # ========== Vision Algorithm(1.06) ==========
   # save image at temp
   def save_out_image_at_temp():
      pass
   # Get avg, max, min
   def status():
      pass
   # upload to mysql
   def upload_mysql():
      pass
   # download from mysql
   def download_mysql():
      pass
   # ========== Vision Algorithm(1.06) Endline ==========
   # ========== Vision Algorithm(1.07) ==========
   # save as csv
   def save_as_csv():
      pass
   # open csv
   def open_csv():
      pass
   # load csv
   def load_csv(fname):
      pass
   # ========== Vision Algorithm(1.07) Endline ==========
   # ========== Vision Algorithm(1.08) ==========
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
   def load_excel(fname):
      pass
   # ========== Vision Algorithm(1.08) Endline ==========

   # ==================== Main code ====================
   if __name__ == '__main__':

      window = tk.Tk()
      window.geometry('1100x600')
      window.title('Computer Vision NumPy(Ver 1.00)')

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
      file_menu.add_command(label='Open RAW file', command=open_image)
      file_menu.add_separator()
      file_menu.add_command(label='Save file', command=save_out_image)

      comvision_menu1 = tk.Menu(main_menu)
      main_menu.add_cascade(label='Pixel', menu=comvision_menu1)
      comvision_menu1.add_command(label='Brighten/Darken', command=add_image)
      comvision_menu1.add_command(label='Contrast', command=rev_image)
      comvision_menu1.add_command(label='Parabola', command=para_image)
      comvision_menu1.add_separator()
      comvision_menu1.add_command(label="Morphing_image", command=morph_image)

      comvision_menu2 = tk.Menu(main_menu)
      main_menu.add_cascade(label='Geometry', menu=comvision_menu2)
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

      window.mainloop()

   ```