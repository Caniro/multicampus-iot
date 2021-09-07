# 리스트 컴프리헨션 문법을 사용하여
# 1에서 100 사이의 짝수로 구성된 리스트를 생성하라.

even_list = [ num for num in range(1, 101) if (num % 2 == 0) ]
print(even_list)
