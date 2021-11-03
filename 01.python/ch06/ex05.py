# 반복문 for

for a in range(5):
    print(a)

for x in range(1, 51):
    if x % 10 == 0:
        print('+', end = '')
    else:
        print('-', end = '')

''' stdout
0
1
2
3
4
---------+---------+---------+---------+---------+%
'''
