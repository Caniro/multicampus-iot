# sum 변수에 총점 356이 저장되어 있고,
# avg 변수에 평균 89.2785가 저장되어 있다.
# 두 변수의 값을 한 문자열로 조립하여 출력하되
# 평균은 반올림하여 소수점 2자리만 출력하라.

sum = 356
avg = 89.2785

str_sum = str(sum)
str_avg = str(round(avg, 2))

result = "총점:" + str_sum + ", 평균:" + str_avg
print(result)
