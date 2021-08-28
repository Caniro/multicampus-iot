dates = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겸살"]
menu = zip(dates, food)
# for d, f in menu:
#     print(f"{d}요일 메뉴 : {f}")

# print(list(enumerate(menu)))
# for idx, (d, f) in list(enumerate(menu)):
#     print(f"{idx}) {d}요일 메뉴 : {f}")

# for _ in menu:
#     print(type(_))

# l = list(menu)
# print(l)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = zip(a, b)
# print(list(c))
# print(list(c))

print(type(menu))
print(menu) # zip은 제너레이터 함수이기 때문에 내용을 미리 볼 수 없다.
