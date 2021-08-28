def multiple_sum(start, end, multiple):
    total = 0
    number = start
    while (True):
        if (number > end):
            break
        if (number % multiple == 0):
            total += number
        number += 1
    return total

print(f"1 ~ 200까지 3의 배수의 합 : {multiple_sum(1, 200, 3)}")
