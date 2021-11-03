# print - 여러 인자, sep, end

a = '고양이'
b = '강아지'
print(a, end = ' ')
print(b)

print(12, 34, 56, sep = '^^', end = ' ---> ')
print(78)

''' stdout
고양이 강아지
12^^34^^56 ---> 78
'''
