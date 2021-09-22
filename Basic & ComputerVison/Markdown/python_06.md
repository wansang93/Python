# 06일차 파이썬 데이터 시각화 190612

## 복습

1주차 : 파이썬 / 기초통계: 데이터베이스, 서버환경, 파이썬 연동, 파이썬 기본

2주차 : 파이썬 데이터 시각화: 컴퓨터 비전(영상처리), 딥러닝, Matplotlib

3주차 : 머신러닝 라이브러리: 컴퓨터비전을 위한 Library

## 파이썬

### 책 : 파이썬 for Beginner

#### 12장 - 객체지향 프로그래밍

1. 클래스

   클래스 생성 -> 인스턴스 생성 -> 필드나 메소드 활용

   클래스 생성

   ``` python
   class Car:
       # field(속성)
       color = ''
       speed = 0
       # method(함수)
       def up_speed(self, value):
           self.speed += value
   ```

   인스턴스 생성

   ``` python
   my_car1 = Car()
   my_car2 = Car()
   my_car1.up_speed(30)
   ```

2. 생성자, 인스턴스 변수와 클래스 변수

   생성자는 \_\_init\_\_() 이라는 이름을 갖는다. init은 Initialize의 약자이다. \_\_(언더바) 2개 붙은 것은 파이썬에서 예약해 놓은것이다. 생성자를 설정하면 인스턴스를 생성할 때 자동으로 생성자를 호출한다.

   ``` python
   class Car:
       color = ''
       speed = 0
       count = 0
       def __init__(self):
           self.color = 'red'
           self.speed = 0
           Car.count += 1  # 클래스 변수
   # 클래스 변수명은 클래스 안에 공간이 할당된 변수를 의미한다.
   ```

   매개변수가 있는 생성자를 만들수도 있다.

   ``` python
   def __init__(self, a, b):
       self.color = a
       self.speed = b
       
   myCar1 = Car('red', 0)
   ```

3. 클래스 상속(Class Inheritance)

   기존 클래스에 있는 필드와 메소드를 그대로 물려받는 새로운 클래스를 만드는 것이다.

   그 중에 메서드 오버라이딩(Overriding)이라는 것이 있는데 상위 클래스의 메서드를 서브 클래스에서 재정의하는 것이다.

   ```python
   class Sedan(Car):
       def up_speed(self, value):
           self.speed += value
           
           if self.speed > 150:
               self.speed = 150
   class Truck(Car):
       pass
   ```

4. 클래스의 특별한 메소드

   ``` python
   def __del__(self):
       print('Destructor(소멸자): 삭제할 때 자동으로 실행')
       
   def __repr__(self):
       return '프린트문을 실행하면 자동으로 실행'
       
   def __add__(self, other):
       return self.a + other.a
   # 인스턴스 사이에 덧셈 작업이 일어날 때 실행
   ```

5. 추상 메소드

   상속받은 서브클래스에서 메소드를 재정의해 사용하는 것을 메소드 오버라이딩이다. 서브 클래스에서 메소드를 오버라이딩해서 사용하려면 슈퍼 클래스에서는 빈 껍질의 메소드만 만들어 놓고 내용은 pass로 채우면 된다. 하지만 문법적으로 큰 문제가 없지만 심각한 논리적인 오류를 발생할 가능성이 있다. 따라서 NotImplementedError()를 raise하는 방식으로 사용하자.

   ``` python
   def method(self):
       raise NotImplementedError()
   ```

6. 멀티 스레드(Thread)

   스레드는 프로그램 하나에서 여러 개를 동시에 처리할 수 있도록 제공하는 기능이다.

   ``` python
   import threading
   ```

7. 멀티 프로세싱

   파이썬에서 스레드는 내부적으로 CPU를 1개만 사용한다. 그래서 동시에 수행하더라도 실질적인 처리 속도는 오히려 더 느려질 수 있다. 반면 멀티 프로세싱 기법은 동시에 CPU를 여러 개 사용한다.

   ``` python
   import multiprocessing
   ```

#### 14장 - 미니 프로젝트(컴퓨터 비전 참고)

### 코드

#### 컴퓨터 비전 흑백 이미지(.raw) 시각화 Version 0.01

- 라이브러리 호출
  
  ``` python
  import tkinter as tk
  import tkinter.simpledialog
  import tkinter.filedialog
  import os
  import math
  ```

- 변수 선언

  ``` python
  # ==================== Global Variable ====================
  window, canvas, paper = None, None, None
  inH, inW, outH, outW = [0] * 4
  inImage, outImage = [], []
  filename = ''
  ```

- 파일 입출력
  
  ``` python
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
  ```

- 컴퓨터 비전 알고리즘

  ``` python
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
  ```

- 메인 코드

  ``` python
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
          
  ```

## 과제

- 기하학 처리
- 오른쪽 90도 회전
- 이동 -->  상하/좌우
- 축소  --> 배율 (2/4/8)
- 확대  --> 배율 (2/4)
- (선택) 회전 --> 각도 입력
