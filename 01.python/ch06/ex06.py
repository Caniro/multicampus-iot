# 필요없는 변수는 _(underscore)에 할당

for _ in range(5):
    print('-' * 9, end='')
    print('+', end = '')

print()
print(_)

''' stdout
---------+---------+---------+---------+---------+
4
'''
