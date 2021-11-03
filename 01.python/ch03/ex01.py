# hex - 숫자를 0x로 시작하는 16진수의 문자열로 변환

print(hex(42))
print(type(hex(42)))
try:
    print(int(hex(42)))
except Exception as e:
    print('error:', e)
try:
    print(oct(hex(42)))
except Exception as e:
    print('error:', e)

a = 0x1a
print(a)

''' stdout
0x2a
<class 'str'>
error: invalid literal for int() with base 10: '0x2a'
error: 'str' object cannot be interpreted as an integer
26
'''
