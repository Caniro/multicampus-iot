import random

direction_list = ["동", "서", "남", "북", "그 외"]
dir = random.choice(direction_list)
print(f"방향 : {dir}")

if (dir == "동"):
    print("강동구")
elif (dir == "서"):
    print("강서구")
elif (dir == "남"):
    print("강남구")
elif (dir == "북"):
    print("강북구")
else:
    print("에러")
