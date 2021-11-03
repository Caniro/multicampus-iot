# 변수의 범위

def kim():
    temp = "김과장의 함수"
    print(temp)

def lee():
    temp = 2 ** 10
    return temp

def park(a):
    temp = a * 2
    print(temp)

kim()
print(lee())
park(6)

''' stdout
김과장의 함수
1024
12
'''
