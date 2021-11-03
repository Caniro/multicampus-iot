# 리스트의 언팩(unpack, splat)

def intsum(*ints):
    print(type(ints))
    print(ints)

    total = 0
    for num in ints:
        total += num
    return total

scores = [20, 30, 40]
# print(intsum(scores)) # 에러
print(intsum(*scores)) # 펼침 : [20, 30, 40] -> 20, 30, 40
print(*scores)

''' stdout
<class 'tuple'>
(20, 30, 40)
90
20 30 40
'''
