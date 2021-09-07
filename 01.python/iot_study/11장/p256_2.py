# price 리스트에 상품 가격 다섯 개가 저장되어 있다.
# 모든 상품의 가격을 20% 세일한 값으로 출력하라.

from random import randrange

price = [randrange(10, 100) * 100 for _ in range(5)]
print(f"정가 : {price}")

sale_rate = 0.2
sale_price = list(map(lambda p:int(p * (1 - sale_rate)), price))
print(f"할인가 : {sale_price}")
