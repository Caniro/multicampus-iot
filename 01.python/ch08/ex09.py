# while (True):
for _ in range(3):
    height = input("키 : ")
    if height.isnumeric():
        height = int(height)
        print("키 =", height)
        break
    else:
        print("숫자만 입력하세요")
