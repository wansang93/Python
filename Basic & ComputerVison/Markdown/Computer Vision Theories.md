# PPT 이론

## 화소점 처리(Pixel)

- 디지털 영상의 원 화소의 값이나 위치를 바탕으로 단일 화솟값을 변경하는 기술
- 산술연산, 논리연산 등을 통해 값을 변경
- 히스토그램(Histogram): 관측 데이터를 한눈에 보기 쉽게 기둥형태의 그래프로 나타내는 것

화소의 밝기 값

- 밝기의 단계 수는 화소를 표현하는 양자화 비트 수가 결정
- 흑백 영상은 색은 없고 밝기만 있음
- 보통 화소의 밝기를 나타내는데 주로 양자화 비트 수를 8비트로 표현

명암 대비

- 대비(Contrast): 영상 내에 있는 가장 밝은 값과 가장 어두운 값의 차이로 영상의 품질을 결정하는데 중요한 요소
- 높은 대비 -> 어두운 명도와 밝은 명도의 차이가 큼 -> 시각적으로 명확하게 보임
- 낮은 대비 -> 어두운 명도와 밝은 명도의 차이가 작음 -> 시각적으로 명확하지 못함

## 산술연산

- 화솟값의 덧셈, 뺄셈, 곱셈, 나눗셈을 하여 밝기를 조절
  $$
  Output(q) = Input(p+\alpha)
  $$
- 클래핑(Clamping) 기법: 최댓값(255) 초과시 255, 최솟값(0) 미만시 0으로 설정
- 랩핑(Wrapng) 기법: 최댓값 초과시 다시 0부터 시작, 최솟값 미만시 다시 255부터 시작

## 논리연산

- 화솟값의 AND 연산(Mask)
  0, 1으로 구성된 이진데이터를 AND연산을 함으로 해당 부분을 버림
  $$
  Output(q) = Input(p) \& MASK(x)
  $$
- 화솟값의 OR 연산(Selective-set)
  0, 1로 구성된 이진데이터를 OR연산을 함으로 선택적으로 값을 추출함
  $$
  Output(q) = Input(p) \| Selective(x)
  $$

- 화솟값의 XOR 연산(Compare)
  입력이 서로 다를 때만 1로 출력함으로 두 데이터를 비교할 때 사용
  $$
  Output(q) = Input(p) \oplus Compare(x)
  $$
- 화솟값의 NOT 연산(Invert)
  영상의 비트를 반전
  $$
  Output(q) = !(Input(p))
  $$

## 화소점 처리 기법

- Null Transform
  $$
  Output(q) = Input(p)
  $$
- Negative Transform
  $$
  Output(q) = 255 - Input(p)
  $$
- Gamma Correction
  $$
  Output(q) = Input(p) * 1 /\Gamma
  $$
- Intensity Contrast Transform
  - Intensity Contrast Stretch
  - Intensity Contrast Compress
- Posterizing
- Binarization
