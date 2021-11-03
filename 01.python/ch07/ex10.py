# 변수의 범위

def kim():
    temp = "김과장의 함수"
    print(temp)

kim()
# print(temp) # NameError: name 'temp' is not defined

''' stdout
김과장의 함수
'''
