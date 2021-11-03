# 반복문 - continue

score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:
        continue
    print(s)
print('성적 처리 끝')

''' stdout
92
86
68
56
성적 처리 끝
'''
