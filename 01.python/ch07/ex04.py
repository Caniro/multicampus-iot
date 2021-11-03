# 함수 - 가변인수

# def intsum(*ints):
def intsum(weight, *ints):
    print(type(ints))
    print(ints)
    total = 0
    for num in ints:
        # total += num
        total += num * weight
    return total

print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))
print(intsum(1))
# print(intsum())

''' stdout
<class 'tuple'>
(2, 3)
5
<class 'tuple'>
(7, 9, 11, 13)
200
<class 'tuple'>
(9, 6, 2, 9, 7, 5, 8)
368
<class 'tuple'>
()
0
'''
