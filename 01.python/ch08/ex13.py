# 포맷 문자열

price = 500
print("궁금하면 " + str(price) + "원!")

month = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." % (month, day, anni))

message = f"{month}월 {day}일은 {anni}이다."
print(message)

height = 12.123456
print(f"키: {height}")
print(f"키: {height:.2f}")
print(f"키: {height:10.3f}")

''' stdout
궁금하면 500원!
8월 15일은 광복절이다.
8월 15일은 광복절이다.
키: 12.123456
키: 12.12
키:     12.123
'''
