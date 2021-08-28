# 1 ~ n 까지의 수에서 3과 4의 공배수를
# 뽑아주는 제너레이터 함수를 작성하세요.
# n은 매개변수로 전달한 값을 사용

def get_common_multiple(n):
    for num in range(1, n + 1):
        if (num % 3 == 0) and (num % 4 == 0):
            yield num

for n in get_common_multiple(100):
    print(n)
