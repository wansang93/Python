import collections

# 일반적인 튜플
p = (10, 20)
print(p[0])
# p[0] = 100  # -> error 발생

# 나의 생각을 적었는데 검증 필요, 아직 미완성
# # Point라는 객체로 생성하여 x값은 외부에서 접근하지 못하게 설정(튜플의 기능처럼)
# class Point(object):
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y

#     def get_x(self):
#         print(self.__x)

# p = Point(x=10, y=20)
# # print(p.x)  # -> error 발생, x를 private로 설정했기 때문에
# print(p.get_x)
# print(p.y)  # 20