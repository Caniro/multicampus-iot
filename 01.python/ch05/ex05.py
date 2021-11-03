# 조건문 - and, or 사용

a = 3
b = 4
if a == 3 and b == 4:
    print("OK")

a = 3
b = 5
if a == 3 or b == 4:
    print("OK")

a = 3
if a > 1 and a < 10:
    print("OK")
if 1 < a < 10:  # 파이썬에서 가능한 기법
    print("OK")

''' stdout
OK
OK
OK
OK
'''
