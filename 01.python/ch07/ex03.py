# 함수

def printsum(n):
    total = 0
    for num in range(n + 1):
        total += num
    print("~", n, "=", total)

printsum(4)
printsum(10)

''' stdout
~ 4 = 10
~ 10 = 55
'''
