# 반복문 예제

# 1 ~ 100의 합
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print('1부터 100까지의 합 :', total)

# 1 ~ 100 중 홀수의 합
total = 0
number = 1
while number <= 100:
    total += number
    number += 2
print('1부터 100 중 홀수의 합 :', total)

# 1 ~ 100 중 3, 5의 공배수를 출력
number = 1
while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print(number, end = ' ')
    number += 1

''' stdout
1부터 100까지의 합 : 5050
1부터 100 중 홀수의 합 : 2500
15 30 45 60 75 90 %   
'''
