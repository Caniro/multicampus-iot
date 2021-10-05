# 시퀀스 데이터로 numpy 배열 생성
import numpy as np

print('numpy version :', np.__version__)

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print('\na1 :', a1)

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print('a2 :', a2)

# 데이터 타입 확인
print('a1.dtype :', a1.dtype)
print('a2.dtype :', a2.dtype)
