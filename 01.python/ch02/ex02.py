# print - 여러 인자, sep, end

a = 12
b = 34
print(a, b)
print(a, b, sep = ', ')
print(a, b, sep = '')
print(a, b, sep = ' -> ', end = '.')

''' stdout
12 34
12, 34
1234
12 -> 34.%       # %은 줄바꿈 없이 끝남을 의미
'''
