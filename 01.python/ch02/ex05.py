# input - 입력 받은 문자열을 수학적으로 연산하려면 형변환 필요

price = input('가격을 입력하세요 : ')
num = input('수량을 입력하세요 : ')
total = int(price) * int(num)

print('총액은 ', total, '원입니다.', sep = '')

''' stdout
가격을 입력하세요 : 3
수량을 입력하세요 : 22
총액은 66원입니다.
'''
