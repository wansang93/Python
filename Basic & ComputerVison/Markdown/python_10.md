# 10일차 파이썬 패키지를 활용한 데이터 시각화 190618

## 복습 및 계획

- 1주차: 데이터베이스, 서버환경, 파이썬 설치, 파이썬 서버 연동
- 2주차: 파이썬 기초, 파이썬 데이터 시각화
- 3주차: 컴퓨터 비전 라이브러리, 머신러닝 라이브러리
- 4주차: 미니 프로젝트 계획 및 발표

## 과제 풀이 및 코드

- 10-01 CSV viewer 02(퀴즈2. Code09-05로 선택된 CSV를 TreeView로 출력하기)

   ``` python
   import tkinter as tk
   import tkinter.filedialog
   from tkinter import ttk
   import csv

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

   if __name__ == "__main__":

      window = tk.Tk()
      window.geometry('400x300')

      sheet = ttk.Treeview(window)

      main_menu = tk.Menu(window)
      window.config(menu=main_menu)

      file_menu = tk.Menu(main_menu)
      main_menu.add_cascade(label="CSV 처리", menu=file_menu)
      file_menu.add_command(label="CSV 열기", command=open_csv)

      window.mainloop()
   ```

### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.07

- 미션1. [CSV 처리] -> [CSV 저장] 메뉴를 선택해서 다음 형식으로 저장하기

   ``` python
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
   ```

- 미션2. [CSV 처리] -> [CSV 열기] 메뉴를 선택해서 위에서 저장한 CSV를 화면에 출력(영상으로 출력)

   ``` python
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
   ```

## Excel

엑셀은 실무에서 사람들이 가장 많이 사용하는 데이터 자료입니다.

따라서 배워두면 좋습니다.

### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.08

- excel로 저장

   ``` python
   import xlsxwriter
   def save_as_excel():
      global window, outImage, outH, outW
      if outImage == []:
         tkinter.messagebox.showinfo(title='Error',
               message='Please open image frist')
         return

      save_fp = tkinter.filedialog.asksaveasfile(
         parent=window,
         mode='wb',
         defaultextension='*.xls',
         filetypes=(('EXCEL file', '*.xls'), ('All file', '*.*')))

      if save_fp == '' or save_fp is None:
         return

      xls_name = save_fp.name
      sheet_name = os.path.basename(xls_name)
      workbook = xlsxwriter.Workbook(xls_name)
      worksheet = workbook.add_worksheet(sheet_name)

      for i in range(outH):
         for j in range(outW):
               worksheet.write(i, j, outImage[i][j])

      workbook.close()
   ```

- excel art로 저장

   ``` python
   def save_as_excel_art():
      global window, outImage, outH, outW
      if outImage == []:
         tkinter.messagebox.showinfo(title='Error',
               message='Please open image frist')
         return

      save_fp = tkinter.filedialog.asksaveasfile(
         parent=window,
         mode='wb',
         defaultextension='*.xls',
         filetypes=(('EXCEL file', '*.xls'), ('All file', '*.*')))
      xls_name = save_fp.name
      sheet_name = os.path.basename(xls_name)
      workbook = xlsxwriter.Workbook(xls_name)
      worksheet = workbook.add_worksheet(sheet_name)

      # 행과 열을 정사각형으로 만들기
      # 열 길이 수정
      worksheet.set_column(0, outH-1, 1.0)
      # 행 길이 수정
      for i in range(outH):
         worksheet.set_row(i, 9.5)

      # 셀에 값을 채워 넣기
      for i in range(outH):
         for j in range(outW):
               data = outImage[i][j]
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
   ```

- excel 읽어오기

   ```python
   def open_excel():
      global window, filename
      filename = tkinter.filedialog.askopenfilename(
         parent=window, filetype=(('EXCEL file', '*.xls;*.xlsx'), ('All file', '*.*')))
      if filename == '' or filename is None:
         return

      load_excel(filename)
      equal_image()

   import xlrd
   def load_excel(f_name):
      global inH, inW, inImage
      workbook = xlrd.open_workbook(f_name)
      worksheet = workbook.sheet_by_index(0)
      inW = worksheet.ncols
      inH = worksheet.nrows
      inImage = []
      inImage = malloc(inH, inW)
      
      for i in range(inH):
         for j in range(inW):
               inImage[i][j] = int(worksheet.cell_value(i, j))
   ```

## NumPy(Numerical Python)

list가 아닌 array를 사용해서 Numerical 계산을 빠르게 수행함

Numpy의 장점
   - 빠르고 메모리를 효율적으로 사용, 벡터 산술연산과 세련된 브로드캐스팅 기능 제공
   - 반복문이 필요 없이 전체 데이터 배열에 대해 빠른 연산을 제공
   - 선형대수, 난수 발생기, 푸리에 변환 가능
   - C, C++, 포트란으로 쓰여진 코드를 통합하는 도구

## 과제

- 퀴즈 1. 숫자로 지정된 엑셀을 읽어서 영상으로 출력하기
- 퀴즈 2. List와 Numpy의 영상 밝게하기 성능 비교
- 미션: 모두 순수 NumPy 버전으로 바꿔보기