# bool 형변환

print(None, bool(None))
print(0, bool(0))
print('', bool(''))
print('False', bool('False'))
print(False, bool(False))
print([], bool([]))
print((), bool(()))

''' stdout
None False
0 False
 False
False True
False False
[] False
() False
'''
