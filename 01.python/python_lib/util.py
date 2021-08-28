INCH = 2.54

def calcsum(n):
    total = 0
    for num in range(n + 1):
        total += num
    return total

# print("util.py", __name__) # 모듈명

if __name__ == "__main__":
    print(f"1 inch = {INCH}")
    print(f"~10 = {calcsum(10)}")
