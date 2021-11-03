# 문자열 함수

# while (True):
for _ in range(3):
    height = input("키 : ")
    if height.isnumeric():
        height = int(height)
        print("키 =", height)
        break
    else:
        print("숫자만 입력하세요")

''' stdout
키 : abc
숫자만 입력하세요
키 : 170
키 = 170
'''
