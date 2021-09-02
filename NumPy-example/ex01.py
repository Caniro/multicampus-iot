# python shell로 한줄씩 테스트
import numpy as np

np.__version__

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
a1

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
a2

a1.dtype
a2.dtype

data3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

data3.shape

np.arange(0, 10, 2)
np.arange(1, 10)
np.arange(5)

np.arange(12).reshape(4, 3)

b1 = np.arange(12).reshape(4,3)
b1.shape

b2 = np.arange(5)
b2.shape

np.linspace(1, 10, 10)
np.linspace(0, np.pi, 20 )

np.zeros(10)
np.zeros((3,4))
np.ones(5)
np.ones((3,5))

np.random.rand(2,3)
np.random.rand()
np.random.rand(2,3,4)

np.random.randint(10, size=(3, 4))
np.random.randint(1, 30)

# 인덱싱
a1 = np.array([0, 10, 20, 30, 40, 50])
a1
a1[0]
a1[4]
a1[5] = 70
a1
a1[[1,3,4]]

a2 = np.arange(10, 100, 10).reshape(3,3)
a2
a2[0, 2]
a2[2, 2] = 95
a2
a2[1]

a2[1] = np.array([45, 55, 65])
a2
a2[1] = [47, 57, 67]
a2
a2[[0, 2], [0, 1]]

a = np.array([1, 2, 3, 4, 5, 6])
a[a > 3]
a[(a % 2) == 0]

b2 = np.arange(10, 100, 10).reshape(3,3)
b2
b2[1:3, 1:3]
b2[:3, 1:]
b2[1][0:2]
