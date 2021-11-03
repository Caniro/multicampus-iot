# 함수

# total = 0
# for i in range(1, 5):
#     total += i
# print('~ 4 =', total)

# total = 0
# for i in range(1, 11):
#     total += i
# print('~ 10 =', total)

def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num
    return total

print("~ 4 =", calcsum(4))
print("~ 10 =", calcsum(10))

''' stdout
~ 4 = 10
~ 10 = 55
'''
