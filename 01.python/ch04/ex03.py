# 숫자, 문자열 연산

a = 5
a += 1
print(a)
a -= 2
print(a)
a *= 2
print(a)

s1 = "대한민국"
s2 = "만세"
print(s1 + s2)

print("싫어 " * 3)
print("=" * 40)

try:
    s = "korea" + 2002
except Exception as e:
    print('error:', e)

''' stdout
6
4
8
대한민국만세
싫어 싫어 싫어 
========================================
error: can only concatenate str (not "int") to str
'''
