# 변수의 범위

price = 1000

def sale():
    # global price # 전역 변수를 변경할 때는 global 키워드 사용
    price = 500

sale()
print(price)

''' stdout
1000
'''
