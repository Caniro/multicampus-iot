# reshape() 메서드, shape 속성
import numpy as np

data1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print('data1 :', data1)
print('data1\'s shape :', data1.shape) # row, col

r1 = data1.reshape(12)
print('\nr1 :', r1)
print('r1\'s shape :', r1.shape) # row, col

r2 = r1.reshape(3, 4)
print('\nr2 :', r2)
print('r2\'s shape :', r2.shape)

r3 = r2.reshape(2, 6)
print('\nr3 :', r3)
print('r3\'s shape :', r3.shape)
