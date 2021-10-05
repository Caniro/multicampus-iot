# numpy.random
import numpy as np

 # 시드 설정 가능
np.random.seed(0)

# [0, 1) 사이 난수 생성
print(np.random.rand())
print(np.random.rand(2, 3))
print(np.random.rand(2, 3, 4))
print(np.random.rand(2, 3, 4, 5))
print()

# 정규 분포 난수
print(np.random.randn(5, 5))
print()

# [low, high) 사이의 정수 난수
print(np.random.randint(1, 30))
print(np.random.randint(0, 10, size=(3, 4)))
print(np.random.randint(10, size=(3, 4)))
