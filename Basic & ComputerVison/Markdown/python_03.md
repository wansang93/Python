# 03일차 파이썬 기본문법 190605

## DataBase

* Data : 처리되기 전의 자료

* Table : Data를 편리하게 관리하기 위해 Table을 사용, Table은 하나의 표라고 생각하면 편함

   * 열 : 열, column, field로 불리고 주로 정보를 나타냄 ex) ID, 이름, 나이, 주소 등

   * 행 : 행, row, record로 불리고 하나의 행은 한 Data의 정보를 나타냄 

      | ID   | 이름   | 주소 |
      | ---- | ------ | ---- |
      | wans | 김완상 | 고양 |
      | hong | 홍길동 | 강남 |

      테이블에는 기본적으로 기본키를 지정해 주면 관리하기 편하다. 

      보통 기본키는 NOT_NULL로 설정하고 Unique한 값으로 정해주고 하나만 정해준다.

      ex) 학번, 주민번호, 회원번호, ID 등등

* Database : Table을 데이터 저장소에 넣음 데이터 저장소가 Database임, 모양은 원통모양

* DBMS : Database를 컴퓨터에서 관리하기위한 소프트웨어 ex) Oracle, MySQL, MariaDB, SSMS 등

   * 데이터를 조작하기 위해서는 Insert(삽입), Update(업데이트), Delete(삭제)를 해야한다. 또 이것을 선택(Select)해서 따로 추출, 조회, 조작, 수정등을 할 수 있다.

### SQL로 Database 구축하기

> SQL(Structured Query Language) is a standard computer language for relational database management and data manipulation.

* 1단계 : DBMS 설치

* 2단계 : 데이터 베이스 구축

  * 데이터 베이스 생성
  
      ```mysql
      CREATE DATABASE samsongDB;
      ```
  
  * 테이블 생성
  
      ```mysql
      USE samsongDB;
      SHOW TABLES;  -- Table들을 보기
      CREATE TABLE userTable(
          userId CHAR(10), userName CHAR(5), userMail VARCHAR(50), birthYear SMALLINT);
      DESCRIBE userTable;  -- userTable의 속성값들 보기
      ```
  
      > SMALLINT와 INT의 차이
      >
      > SMALLINT : 2bit(-32,768~32,767), INT : 4bit(약 -21억 4700만에서 21억 4700만)
  
      > VARCHAR와 CHAR의 차이
      >
      > 동적으로 글자수를 잡아 공간낭비가 없음, 하지만 불러오는 속도에서는 차이가 있음
      >
      > 하지만 또 Oracle에서 속도차이가 없게 만들었고 다른 DBMS는 속도차이가 조금 있을 수 있음
  
  * 데이터 입력
  
      ```mysql
      -- 실무에서는 이렇게 작성
      INSERT INTO userTable(userId, userName, userMail, birthYear)
      VALUS('wansang93', N'김완상', 'wansang93@naver.com', '1993')
      VALUS('wansangbaby', N'김완상2세', 'wansangbaby24@naver.com', '2024')
      -- N은 유니코드 호환성을 높임
      
      -- 간편하게는 이렇게 작성
      INSERT INTO userTable VALUES( 'AAA', '에이', 'aa@aa.com', '1995');
      INSERT INTO userTable VALUES( 'BBB', '비비', 'bb@bb.com', '1991');
      INSERT INTO userTable VALUES( 'CCC', '씨씨', 'cc@cc.com', '1988');
      COMMIT;
      ```
  
      > COMMIT은 INSERT한 것을 저장한다는 개념이다. 반대되는 단어는 ROLLBACK 이다.
  
* 3단계 : 응용 프로그램에서 구축된 데이터 활용

  * 데이터 조회 및 활용
  
      ```mysql
      -- 실무에서는 SELECT 전체(*)를 하는것보다 원하는 값을 치는것을 권유함
        SELECT * FROM userTable;
        SELECT * FROM userTable WHERE userID = 'BBB';
        SELECT userName, userMail From userTable WHERE userID = 'BBB';
        SELECT userName, birthYear FROM userTable WHERE birthYear < 1995;
      -- 선택 전체(*) ~로 부터 userTable
      -- 선택 전체(*) ~로 부터 userTable 어디서?(조건) userID가 BBB 인거
      -- 선택 userName, userMail ~로 부터 userTable 어디서?(조건) userID 가 BBB인거
      -- 선택 userName, birthYear ~로 부터 userTable 어디서?(조건) birthYear < 1995
      ```

## 파이썬

### 선생님 파이썬 코딩 팁

* 코딩할 때 주석을 많이 달고 범용적으로 코딩하면 좋다.

* 함수부분, 전역변수부분, 메인코드부분으로 나눠서 코딩하면 좋다.

* 파이썬처럼 프로그래밍해도 되고 다른언어처럼 코딩하면 다른언어 사용자가 이해하기 쉽다.

  * Python Enhance Proposal-8(PEP-8) : 파이썬에서 코딩할 때 공통적으로 지키자는 룰을 만들었다.
  * Google Java Style Guide : 구글에서 코딩할 때 스타일을 가이드 한 것이다.

###  책 : 파이썬 for Beginner

#### 13장 - 데이터베이스

* SQLite Data 입력

  ``` python
  import sqlite3
  
  conn = sqlite3.connect("samsongDB")  # 1. DB 연결
  cur = conn.cursor()  # 2. 커서 생성
  # 3. 하고 싶은 것 실행
  sql = "Create TABLE IF NOT EXISTS userTable(userId INT, userName CHAR(5))"
  cur.execute(sql)
  
  sql2 = "INSERT INTO userTable VALUES( 1, '홍길동')"
  cur.execute(sql2)
  sql3 = "INSERT INTO userTable VALUES( 2, '이순신')"
  cur.execute(sql3)
  
  cur.close()  # 4. 커서 종료
  conn.commit()  # 5. 데이터를 수정했을 때 반드시 커밋을 해야 DB안의 내용이 수정됨
  conn.close()  # 6. DB 연결 종료
  print('OK~')
  
  ```

* SQLite Data 조회

  ``` python
  import sqlite3
  
  conn = sqlite3.connect("samsongDB")  # 1. DB 연결
  cur = conn.cursor()  # 2. 커서 생성(트럭, 연결로프)
  # 3. 하고 싶은 것 실행
  sql = "SELECT * FROM userTable"
  cur.execute(sql)
  # 조회 방법이 2가지가 있음
  # 전부 다 가져오기
  rows = cur.fetchall()
  print(rows)
  # 한개식 당기기
  while True:
      rows = cur.fetchone()
      print(rows)
      break
  
  cur.close()  # 4. 커서 종료
  conn.close()  # 5. DB 연결 종료
  print('OK~')  # 잘 되었는지 프린트 문으로 확인
  ```
  
  > 한개씩 가져오면 무수히 많은 데이터들을 불러드릴때 오류 발생의 가능성이 줄어든다.
  >
  > 한번에 어려개를 가져오면 코딩은 쉬우나 메모리나 시스템적으로 오류가 발생할 가능성이 있다.


#### 2장 - 미리 만드는 쓸만한 프로그램

* print(), input() 함수 사용과 %d, %f

  ``` python
  print("Hello World")  # 화면에 출력
  a = int(input("첫번째 숫자를 입력하세요 : "))  # a에 첫번째 입력받은 값을 int로 변환하여 대입
  b = int(input("첫번째 숫자를 입력하세요 : "))
  result = a+b
  
  print("%d, %d " % (a, b))
  print("%4d+%04d = %7.3f" % (a, b, result))
  ```
  
  > %4d는 int값을 4자리공간으로 표현
  >
  > %04d는 int값을 4자리공간으로 표현하고 빈공간일 경우 0으로 대입
  >
  > %7.3f는 float값을 7자리공간으로 표현하고 소숫점 3자리까지 표현 소숫점 빈공간은 0으로 대입

#### 3장 - 변수와 데이터

1. print() 를 사용한 다양한 출력

   * format을 활용한 함수 출력

     ``` python
     print("{0:d} {1:5d} \n".format(100, 200))  
     print("{1:f} {0:d}".format(100, 200))
     print("-" * 50, end=" df")
     ```

     > format 안의 값의 0번째를, %d로 1번째 값을 5자리공간으로 1번째 값을 넣어라
     >
     > format 안의 값의 1번째를, %f로 1번째 값을 0번째 값을 넣어라
     >
     > "-" 라는 문자열을 50번 반복하고 마지막에 _df를 출력해라

   * 문자열에서 \를 치면 escape characters(특수한 동작)가 실행된다.

     ``` python
     print("\n, \t, \b \\, \"")
     print('\a, \f, \r \N{name}, \'')
     print("\110\145\154\154\157\40\127\157\162\154\144\41", "\x41\x42\x43")
     ```

     > line feed(enter), tab, backspace, backslash, double quotation(Quotation Mark)
     >
     > bell, Formfeed, carriage return, name in the Unicode database, Single Quotation(Apostrophe),
     >
     > Character with octal value OOO, Character with hexa value HH

2. 변수의 선언과 사용

   1. 변수란?

      변수는 파이썬에서는 개체를 다루는 포인터이다.

      정적 프로토타이핑 언어인 C/C++와는 달리 특별히 변수를 미리 선언하지 않아도 된다.

      파이썬은 실행 시점에 변수형(type)이 정해지기 때문에 동적 프로토타이핑 언어라고 말한다.

   2. 변수명 규칙

      변수명에는 영문자(대소문자는 구분), 한글,  숫자를 사용, <u>특수문자는 사용 불가</u>하다.

      <u>첫자리에 숫자는 사용 불가</u>하다.

      <u>파이썬 키워드는 변수명으로 사용불가</u>하다.

      > and, as, assert, break, class, continue, def, del, False, if, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, Ture, try, while, with, yield

   3. 변수 삭제하기

      파이썬은 동적 프로토타이핑 언어인만큼 한번 값이 대입된 변수는 프로그램이 종료될때까지 유지될 가능성이 크다.
      
      물론 함수등 특정 범위내에서만 동작하고 그 함수에서 빠져나오면 사라진다.
      
      하지만 프로그래머의 의도에 따라 강제로 변수를 삭제할 수도 있다.

      ``` python
      del(변수명)
      ```

   4. 변수형(type) 보기와 변수별 사이즈 보기

      ``` python
      type(변수명)
      # 변수의 사이즈를 보려면 need to import sys
      import sys
      sys.getsizeof(변수명)
      intVar = 0  # 12
      floatVar = 0.0  # 16
      boolVar = True  # 14
      strVar = ""  # 25
      listVar = []  # 36
      tupleVar = ()  # 28
      dictVar = {}  # 136
      setVar = set()  # 116
      ```

3. 데이터 표현 단위와 진수 전환

   1. Bit and Byte

      컴퓨터에서 표현할 수 있는 가장 작은 단위는 Bit, 8Bit가 보이면 Byte이다.

   2. 2진수와 16진수

      파이썬은 2진수, 8진수, 16진수를 변환하는 함수를 제공한다.

      ``` python
      bin(숫자), oct(숫자), hex(숫자)
      
      char = "ff"
      num10 = int(char, 16)
      
      print(num10)
      print(hex(num10))
      ```

      > int(char, 16)은 char를 16진수로 읽어서 10진수로 만든다.

#### 4장 - 연산자

1. 산술 연산자 : +, -, *, /, //(나누기 몫), %(나머지 값), **(제곱)
2. 관계 연산자 : ==, !=
3. 논리 연산자 : and, or, not
4. 비트 연산자 : &(and), |(or), ^(xor), ~(not), <<(비트 왼쪽으로 이동), >>(비트 오른쪽으로 이동)

## 코드

- 03-01 SQLite 데이터 입력
- 03-02 SQLite 데이터 조회
- 03-03 계산기
- 03-04 동전 교환
- 03-05 if문 응용
- 03-06 if문 응용
- 03-07 while문
- 03-08 Lotto 추첨
- 03-09 MySQL Data 입력
- 03-10 MySQL Data 조회

## 과제

- Windows Server의 MariaDB or MySQL에 p.423 구현
- SQL Server에 p.423 구현

