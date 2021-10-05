# 배열 타입 변환
import numpy as np

str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
print(str_a1, '\t', str_a1.dtype)
print(num_a1, '\t', num_a1.dtype)

# print(str_a1.dtype)
# print(num_a1.dtype)
# <U5 : 리틀엔디안(<) 유니코드(U) 문자수:5

str_a1[0] = '1.23456789' # U5 타입이라 5글자까지 보존
print(str_a1, '\t', str_a1.dtype)

num_a2 = num_a1.astype(int)
print(num_a2, '\t', num_a2.dtype)

'''
b : 불
i : 부호가 있는 정수
u : 부호가 없는 정수
f : 실수
c : 복소수
M : 날짜
O : 파이썬 객체
S 혹은 a : 바이트 배열
U : 유니코드
'''
