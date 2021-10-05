# 통계 연산
import numpy as np

arr = np.arange(1, 6)
print(arr)
print('sum :', arr.sum())
print('mean :', arr.mean())
print('standard deviation :', arr.std())
print('variance :', arr.var())
print('min :', arr.min())
print('max :', arr.max())
print('누적 합 :', arr.cumsum())
print('누적 곱 :', arr.cumprod())
