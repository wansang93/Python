# 09일차 파이썬 데이터 시각화 190617

## 계획

- 3주차: 데이터 시각화(컴퓨터 비전) + 데이터베이스 연계
  - 이미지 데이터와 DB 저장 및 연동
  - 대용량 이미지 데이터의 처리 기법
  - 히스토그램 데이터 시각화
- 4주차: 파이썬 라이브러리를 활용한 데이터 분석 / 시각화
  - 내부 라이브러리: CSV, JSON
  - 외부 라이브러리: Numpy, Pandas, Matplotlib
  - EXCEL 데이터 분석/처리(기업에서 많이 쓰이는 데이터 형식)
  - BeautifulSoup: 데이터 수집
  - Pillow: 칼러 이미지 데이터 처리
  - Scikit-learn: 머신러닝/딥러닝 기반의 이미지 데이터 분석/시각화
  - OpenCV, Numpy, scipy 등의 라이브러리 사용
  - Haar-Cascade: 얼굴인식, 코, 눈, 입, 고양이 등 인식가능
  - object-detection-deep-learning: 딥러닝 기반의 정지영상 사물 인식
  - object-detection-deep-learning: 딥러닝 기반의 동영상 사물 인식

## MySQL 데이터 테이블 관리

``` sql
USE bigdata_db;
-- table 정보보기
SHOW TABLES;
DESC rawimage_tbl;
-- table 삭제하기
DROP TABLE rawimage_tbl;
-- table 다시 만들기(raw_avg, raw_max, raw_min)
CREATE TABLE rawimage_tbl
(raw_id INT AUTO_INCREMENT PRIMARY KEY, raw_height smallint, raw_width smallint, raw_fname VARCHAR(30), raw_extname CHAR(5), raw_update DATE, raw_uploader VARCHAR(20), raw_avg TINYINT UNSIGNED, raw_max TINYINT UNSIGNED, raw_min TINYINT UNSIGNED, raw_data LONGBLOB);
```

## 과제 풀이 및 코드

### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.05

- 디스플레이 이미지에서 대용량 파일의 경우, 일정 크기로 보이게 하기

    ``` python
    # ==================== Global Variable ====================
    VIEW_X, VIEW_Y = 512, 512

    # ==================== Function Declaration ====================
    # ========== file I/O ==========
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
    ```

- 히스토그램 데이터 시각화 기능을 matplotlib 없이 직접 구현하기

    ``` python
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

        # ==================== Main code ====================
        comVisionMenu2.add_command(label='Histogram_custom', command=histogram_image_custom)
    ```

- MySQL에 RAW파일 업로드 / 다운로드 하기

  - 선택 기능 1: RAW 파일의 평균, 최대값, 최소값도 계산되어 업로드

    ``` python
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
    ```

  - 선택 기능 2: 특정 폴더를 선택하면 해당 폴더의 RAW 파일이 모두 업로드 되기

    ``` python
    # Global Variable
    raw_file_list = []

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


    def upload_file():
        global raw_file_list

        # DB 연결
        con = pymysql.connect(host=IP_ADDR, user=USER_NAME,
            password=USER_PW, db=DB_NAME, charset=CHAR_SET)
        cur =con.cursor()

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
            a, b, c = find_state(full_name, height, width)

            # sql 작성
            sql = ('INSERT INTO rawimage_tbl(raw_id, raw_height, raw_width, '
                'raw_fname, raw_extname, raw_update, raw_uploader, raw_avg, raw_max, raw_min, raw_data) '
                f'VALUES(NULL, {str(height)}, {str(width)}, '
                f'"{fname}", "{extname}", "{up_date}", "{up_user}", {a}, {b}, {c}, %s);')
            print(sql)

            # 서버로 보내기
            cur.execute(sql, (bin_data,))
            con.commit()

        # 서버 종료
        cur.close()
        con.close()
    ```

- 컴퓨터 비전 툴이 데이터베이스에서 처리되도록 하기

  - 기능 1: outImage 저장하고 DB에 넣기

    ``` python
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
                message='Please Open image frist')
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
    ```

  - 기능 2: DB의 사진 불러오기

    ``` python
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
    ```

### CSV 입문

- 09-04 CSV 01

    ``` python
    import csv
    ## 우리회사 연봉 평균은?

    file_path = r'D:\☆☆☆멀캠생활\Image\csv\emp.csv'

    with open(file_path) as rfp:
        # 방법2
        reader = csv.reader(rfp)
        header_list = next(reader)
        sum = 0
        count = 0
        for cList in reader:
            sum += int(cList[3])
            count += 1
        avg = sum // count
        print('평균연봉:', avg)

        # 방법1
        sum = 0
        line = rfp.readline()
        count = 0
        while True:
            line = rfp.readline()
            if not line:
                break
            count += 1
            line_list = line.split(',')
            sum += int(line_list[3])
        avg = sum // count
        print(avg)
    ```

- 09-05 CSV02

    ``` python
    import csv
    import tkinter.filedialog

    # file_name = tkinter.filedialog.askopenfilename(parent=None,
    #             filetypes=(('csv file', '*.csv'), ('all file', '*.*')))

    file_name = r'D:/☆☆☆멀캠생활/image/csv/supplier_data.csv'

    # 참고 파일
    """
    Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
    Supplier X,001-1001,2341,$500.00,1/20/14
    Supplier X,001-1001,2341,$500.00,1/20/14
    Supplier X,001-1001,5467,$750.00,1/20/14
    Supplier X,001-1001,5467,$750.00,1/20/14
    Supplier Y,50-9501,7009,$250.00,1/30/14
    Supplier Y,50-9501,7009,$250.00,1/30/14
    Supplier Y,50-9505,6650,$125.00,2/3/14
    Supplier Y,50-9505,6650,$125.00,2/3/14
    Supplier Z,920-4803,3321,$615.00,2/3/14
    Supplier Z,920-4804,3321,$615.00,2/10/14
    Supplier Z,920-4805,3321,$615.00,2/17/14
    Supplier Z,920-4806,3321,$615.00,2/24/14
    """

    # 파일을 읽어서 리스트로 저장
    csv_list = []
    with open(file_name) as rfp:
        reader = csv.reader(rfp)
        header_list = next(reader)
        for line in reader:
            csv_list.append(line)

    # 가격 10% 인상시키기
    header_list = [data.upper().strip() for data in header_list]
    pos = header_list.index('COST')

    for i in range(len(csv_list)):
        cost = float(csv_list[i][pos][1:])
        cost *= 1.1
        cost_str = f'{cost:.2f}'
        csv_list[i][pos] = cost_str
    print(csv_list)

    # 결과 저장하기
    save_fp = tkinter.filedialog.asksaveasfile(
        parent=None,
        mode='wt',
        defaultextension='*.csv',
        filetypes=(('csv file', '*.csv'), ('all file', '*.*'))
        )

    with open(save_fp.name, mode='w', newline='') as wfp:
        writer = csv.writer(wfp)
        writer.writerow(tuple(header_list))
        for row in csv_list:
            writer.writerow(row)
    ```

- 09-06 CSV viewer 01

    ``` python
    import tkinter as tk
    from tkinter import ttk

    window = tk.Tk()
    window.geometry('400x300')

    sheet = ttk.Treeview(window)

    # 첫 번째 열 해더 만들기
    sheet.column('#0', width=70)  # 첫 번째 칼럼 내부 이름
    sheet.heading('#0', text='제목1')

    # 두 번째 열 이후 해더 만들기
    sheet['columns'] = ('a', 'b', 'c')
    sheet.column('a', width=70)
    sheet.column('b', width=70)
    sheet.column('c', width=70)

    sheet.heading('a', text='제목2')
    sheet.heading('b', text='제목3')
    sheet.heading('c', text='제목4')
    sheet.pack()

    # 내용 채우기
    sheet.insert('', 'end', text='1열1값', value=('1열1값', '1열2값', '1열3값'))
    sheet.insert('', 'end', text='2열1값', value=('2열2값', '2열2값', '2열3값'))
    sheet.insert('', 'end', text='3열1값', value=('3열3값', '3열2값', '3열3값'))

    window.mainloop()
    ```

## 미션

퀴즈1. MySQL에 저장하기 / 불러오기 추가하기(Code09-03)

퀴즈2. Code09-05로 선택된 CSV를 TreeView로 출력하기

미션1. [컴퓨터 비전]에 [CSV 처리] -> [CSV 저장] 메뉴를 선택해서 다음 형식으로 저장하기

```text
ROW, COLUMN, VALUE(이 행은 생략)
​0, 0, 123
​0, 1, 111
\~~~~
511, 511, 99
```

미션2. [CSV 처리] -> [CSV 열기] 메뉴를 선택해서 위에서 저장한 CSV를 화면에 출력(영상으로 출력)
