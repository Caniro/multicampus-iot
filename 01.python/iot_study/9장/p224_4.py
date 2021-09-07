# [n*n for n in range(1, 10) if n % 3 == 0]
# 위 구문을 평이한 루프와 조건문, 연산식으로 풀어서 작성하라.

original = [n*n for n in range(1, 10) if n % 3 == 0]
print(f"원본 리스트 : {original}")
# print(type(original))

result = []

for n in range(1, 10):
    if (n % 3 == 0):
        result.append(n * n)
print(f"풀어서 작성 : {result}")
# print(type(result))
