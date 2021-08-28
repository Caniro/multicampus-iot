# 1 ~ 100의 합

# sum = 0
# number = 1
# while (number <= 100):
#     sum += number
#     number += 1

# print('1부터 100까지의 합 :', sum)


# 1 ~ 100 중 홀수의 합

# sum = 0
# number = 1
# while (number <= 100):
#     sum += number
#     number += 2

# print('1부터 100 중 홀수의 합 :', sum)


# 1 ~ 100 중 3, 5의 공배수를 출력

# number = 1
# while (number <= 100):
#     if (number % 3 == 0 and number % 5 == 0):
#         print(number, end = ' ')
#     number += 1


# 1 ~ 100 중 홀수의 합 (if문 없이)

sum = 0
number = 1
while (number <= 100):
    sum += number
    number += 2
print(sum)
