# 1 ~ 10 정수의 리스트 a와 
# 각 정수의 제곱의 리스트 b를 만든 후 
# 두 리스트를 합쳐 사전으로 만들고 
# 6의 제곱을 검색하여 출력하라.

a = [n for n in range(1, 11)]
b = list(map(lambda n:n ** 2, a))
print(f"a : {a}")
print(f"b : {b}")

squared_dict = dict(zip(a, b))
print(squared_dict)

squared = squared_dict.get(6)
if (squared):
    print(f"6의 제곱 : {squared}")
else:
    print("해당 값이 존재하지 않습니다.")
