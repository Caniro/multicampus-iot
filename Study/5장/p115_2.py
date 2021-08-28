capital = input("한국의 수도는 ? ")

answer_list = ["서울", "seoul"]

for ans in answer_list:
    if (capital.strip().lower() == ans):
        print("정답! 축하합니다")
