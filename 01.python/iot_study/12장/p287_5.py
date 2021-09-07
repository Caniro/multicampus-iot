# 10에서 20 사이의 난수 10개를 뽑아 출력하라.
# 끝수인 20도 포함한다.

from random import randint

def get_random_list(begin, end, amount):
    random_list = [randint(begin, end) for _ in range(amount)]
    return random_list

begin = 10
end = 20
amount = 10

print(get_random_list(begin, end, amount))
