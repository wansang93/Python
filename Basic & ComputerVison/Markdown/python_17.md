# 17일차 190627

프로젝트 마무리 및 PPT 작성

## 팁들

google colab : GPU 지원해주는 구글 클라우트 파이썬노트북! 함써보자

모두의 알고리즘

빨리 발전하는 공부법 : 가장 쉬운 책으로 시작해서 그 과정을 끝내라! : 단계별 공부법

- 복습 및 정리

  - sqlite : 탑재된 파일 디비

    - 커넥션 - 커서 - 쿼리문 - 날리고 - 쓰고 - 커서닫고 - 커넥션 닫고

  - map함수 (iterator 객체)

    - mylist = [1,2,3,3,4] #요런식으로 사용
    - mylist = list(map(lambda num : num +10, mylist))

  - 템플릿을 깔끔하게 만들어서 GUI를 사용하라!

  - code 05-05 

    - ```python
      import osfor dirName, subDirList, fnames in os.walk('C:/images'): #이 밑에 폴더들 싹다 긁어서 가져옴 (딕셔너리 형식?)    
      for fname in fnames:        
      	if os.path.splitext(fname)[1].upper() == '.GIF': # 확장자 긁어낼 때 : splitext / 디렉터리 네임이랑 파일네임 구분하려면 : 그냥 split            				print(os.path.join(dirName,fname))            
      		print(fname)
      ```

  - 메모장도 만들 수 있다 : app : 메모장! Code05-08

- 우리가 배운 컴퓨터 비전 기술들을 cutomizing이 필요한 파트에서 빛을 발한다!

  - 보간법 등 : 라이브러리를 쓰다가 어려운 상황에 빛남!

- DB에 넣어주기 : Blob 파일로 저장?

  - 근데 Blob으로 넣는게 아니라 파일 하나 Row column을 바로 바꿔줄 수도 있겠지? 되게 빠르겠다

- csv 데이터들 자동화해서 dataframe으로 불러와서 처리할 수 있다 : 자동화!

- numpy

- scikit-learn : 머신러닝 : 모델 clf 만들고 : 학습시키고 : 정답률 구하기

  - 뭐 학습된 모델 가져올 수도 있고
  - Mnist마냥 자음 쓴거 알아보기? : ㄱㄴㄷㄹ... 인식하기!

- openCV에다가 훈련된 딥러님 모델 땡겨와서 실제로 얼굴 인식