# 정의되지 않은 변수 사용

a = (1 + 2) * 3
c = 2
try:
    b = c * d + e
except Exception as e:
    print('error:', e)

''' stdout
error: name 'd' is not defined
'''
