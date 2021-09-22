# 14일차 190624

<https://blog.naver.com/beyondlegend>

인공지능이 가장 큰 분류고,

그 머신러닝이 있고 그 안에 딥러닝도 머신러닝의 일종이에요

머신러닝은 크게 지도학습과 비지도학습이 있어요

사람들 눈이 너무 높아서,

1번은 툴을 써서 구현하는 것
그리고 여유를 만들어서 툴을 써서 구현했던 것을 직접 구현해보는 것

쉬운걸 많이 보는 것이 좋습니다.
이 분야가 빨리 봐야하고 넓게 봐야하는 것이 더 좋습니다.

로맨스 영화는 껴앉는 영화가 많고, 싸우는 영화는 싸우는 횟수가 많을 거에요

근처에 있는게 뭐가 있는지

조심할 것은 그 데이터에만 맞는거에요. 다른 데이터에는 안 맞을 수 있어요

단순하게 말해볼까? 날씨를 90% 이상 맞추는 것이 있어요. 그런데, 사막에 이걸 갖다 팔면은 되겠어요?

거기는 원래 비가 안와!

scikit-learn에서 warning이 약간 뜨더라도 무시하고 그냥 넘어가시는 것도 괜찮아요!

pandas는 numpy와 굉장히 밀접한 친구에요

## SVM 종류

```python
svm.LinearSVR()
svm.SVR()
svm.NuSVC()
svm.SVC()
```

하르케스케이드가 한번만 학습하고 저장시키는 방법(얼굴)

google에서 classifier로 검색하면

분류가 어떻게 되는지 나옴.

그림에서 어떤 것이 분류가 잘 되는지 확인할 수 있음

인공지능 및 딥러닝 이론 잘 이해하고 툴을 써서 결과 도출해보기
툴을 사용하지 않고 직접 구현해보기
머신러닝 / 딥러닝 이론
참고자료 : <https://blog.naver.com/beyondlegend/221338876143>
지도학습
입력값(x)과 정답(t, label)을 포함하는 Training Data를 이용하여 학습하고, 그 학습된 결과를 바탕으로 미지의 데이터에 대해 미래 값 예측하는 방법 => 대부분 머신러닝 문제는 지도학습에 해당됨
지도학습은 학습결과를 바탕으로, 미래의 무엇을 예측하느냐에 따라 회귀, 분류 등으로 구분할 수 있음
회귀 (Regression)
Training Data를 이용하여 연속적인 (숫자) 값을 예측
분류 (Classfication)
Training Data를 이용하여 주어진 입력값이 어떤 종류의 값인지 구별

scikit-learn
참고자료 : 파이썬 라이브러리를 활용한 머신러닝 교재
scikit-learn 사용자 가이드 : <https://scikit-learn.org/stable/user_guide.html>
scikit-learn : 현재 파이썬으로 구현된 가장 유명한 기계 학습 오픈 소스 라이브러리로 오픈소스이며, Numpy와 SciPy를 기반으로 만들어짐
NumPy : 다차원 배열을 위한 기능과 선형 대수 연산과 푸리에 변환 같은 고수준 수학 함수와 유사 난수 생성기를 포함
SciPy : 과학 계산용 함수를 모아놓은 파이썬 패키지, 고성능 선형대수, 함수 최적화, 신호 처리, 특수한 수학 함수와 통계 분포 등을 포함한 많은 기능 제공
NumPy, SciPy, matplotib, Pandas, scikit-learn, scikit-image 설치

Pandas 기본 예제
Data Frame : 표 같은 스프레드 시트 형식의 자료구조, Series 들의 집합
Series : 일련의 객체를 담을 수 있는 1차원 배열 같은 자료구조 (Array, Vector와 같은 형식)

## 과제

- 퀴즈 1. And 게이트를 훈련 시키고 결과를 보자.
- 미션 1. [MNIST GUI 툴] 완성하기
  - 데이터 개수, 분류기를 선택해서 덤프파일을 골고루 만들고 성능이 좋은 분류기를 고민해보기
  - <심화> 분류기도 선택(?) 참고 자료 -> <https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html>