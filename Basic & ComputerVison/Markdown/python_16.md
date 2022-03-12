# 16일차 190626

## 노엘버드

## 16일차 총정리

1. 컴퓨터: H/W + S/W
   1. H/W: CPU, RAM, SSD(HDD), GPU
   2. S/W: OS(Unix, Linux, Windows, Mac)
   3. Windows: 개인용(ex. 홈 에디션), 업무용(ex. 프로페셔널, 엔터프라이즈 에디션), 서버용
2. 파이썬 기초통계
   1. 컴파일러(c/c++, java), 인터프리터(스크립트)
   2. 파이썬 문법(자료구조, 리스트/튜플/딕셔너리)
   3. Database: Oracle, SQL Server, My SQL(MariaDB)
   4. DBMS, DB, Table, Column, Row(Record), Primary Key
   5. SQL: SELECT / INSERT / UPDATE / DELETE / CREATE / DROP / ALTER / GRANT / REVOKE
   6. Python <--> DB연동(파일처리)
   7. 리스트 조작(*), 2차 리스트
   8. 함수(=메소드), 전역 변수 활용(m_xxx(멤버 변수))
   9. GUI 프로그래밍, Menu, 아이콘
   10. 파일처리, 객체지향
   11. 컴퓨터 비전, 알고리즘, 프로그래밍 기법 
3. 파이썬 라이브러리
   1. numpy, matplotlib, pandas(엑셀, DB테이블)
4. scikit-learn 머신러닝
   1. 데이터 준비, 정제, 분석
   2. 분류기 선택(머신러닝 알고리즘)
   3. 훈련: 시간
   4. 결과(모델) --> 저장
   5. 예측, (정답률)
5. 저장된 모델을 활용
   1. 컴퓨터 비전: 직접 구현, Pillow, OpenCV(*)
   2. MNIST --> 직접 훈련 --> 결과 예측(GUI)
   3. 하르케스케이드 --> 얼굴인식(저장된 모델) --> 얼굴, 입, 코, 고양이 ~~~~
   4. MobileNetSSD --> 사물인식 모델 --> CAFFE형식 --> OpenCV 최신버전에서 로딩
   5. 

작은 실패를 많이 해서, 단련을 많이해야합니다.

정원혁 강사님 SQL server로 유명하신분임. 우리나라에서 가장 잘했음

회사에서 비용을 줄여야하는데, 비용 상관없이 돈 쓰는 사람들 별로 안 좋습니다.

회사에서 카드를 줘도 다 쓰면 안됩니다. 구조조정 1순위입니다. 

단점을 보완하면 열심히 해도, 중간밖에 안돼요.
싫은 것을 먼저 지우고 남는 것이 본인의 장점이에요.

성실과 성품이 더욱 중요하다.

- 쉰들러 리스트
- 라스트 모히칸

미션: 딥러닝 활용 컴퓨터 비전 --> 002.mp4 (쇼생크)
 - 최대 사람이 출연한 화면을 캡쳐(최대 인원, 정답률) ==> ?
 - 평활화 처리를 추가한 동여상 인식 ==> ?
 - 내부적으로만 평활화 하고, 보이는 것은 원영상
 - 최대 출연자 화면에서 각 출연자마다 사람을 저장하기
 - 출연자마다 저장되기 전에, 얼굴인식 하기

또는 미니 프로젝트 진행

## 개발개발

## 륜서니

16일차 (scikit-learn 머신 러닝)
총 정리

컴퓨터 : H/W + S/W
H/W : CPU, RAM, SSD(HDD), GPU(그래픽카드)
S/W : OS (Unix, Linux, Windows, Mac)
Windows : 개인용, 업무용, 서버용
파이썬과 기초통계
컴파일러(c/c++, java), 인터프리터(스트립트)
파이썬 문법 (자료구조, 리스트/튜플, 딕셔너리)
Database : Oracle, SQL Server, MySQL(Mariadb)
DBMS, DB, Table, Column, Row(Record), Primary Key(PK)
SQL : SELECT, INSERT/DELETE/UPDATA, CREATE/DROP/ALTER,GRANT/REVOKE
Python <----> DB 연동 (파일처리)
리스트 조작(*), 2차 리스트
함수(=메소드), 전역 변수 활용(m_xxx : 전역 변수 형태)
GUI 프로그래밍, Menu, 아이콘
파일처리, 객제지향
컴퓨터 비전, 알고리즘, 프로그래밍 기법
파이썬 라이브러리
numpy, matplotlib, pandas(엑셀, DB테이블)
scikit-learn 머신 러닝
데이터 준비, 정제, 분석
분류기 선택 (머신러닝 알고리즘)
훈련 : 시간
결과 (모델) ----> 저장
예측, (정답률)
저장된 모델을 활용
컴퓨터 비전 : 직접 구현, Pillow, OpenCV(*)
MNIST --> 직접 훈련 --> 결과 예측 (GUI)
하르케스케이드 --> 얼굴인식 (저장된 모델) ==> OpenCV랑 연결 ----> 얼굴, 입, 코, 고양이~~~~
MibileNETSSD --> 사물인식 모델 --> CAFFE 형식으로 제공 --> OpenCV 최신버전에서 로딩 가능

미션(16일차) <심화>

- 딥러닝 활용 컴퓨터 비전 --> 002.mp4(쇼생크)
- 최대 사람이 출연한 화면을 캡처 (최대인원,정답률) ==> ?
- 평활화 처리를 추가한 동영상 인식 ==> ?
- 내부적으로만 평활화하고, 보이는 것은 원영상
- 최대 출연자 화면에서 각 출연자마다 사람을 저장하기
- 출연자마다 저장되기 전에, 얼굴인식 하기
- 또는 미니 프로젝트 진행