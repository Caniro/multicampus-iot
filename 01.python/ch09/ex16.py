# 리스트와 검색 값을 인수로 받아서
# 검색 값이 있으면 해당 인덱스를, 없으면 -1을 반환하는 함수

def find_value(list_in, value_to_find):
    for index in range(len(list_in)):
        if (list_in[index] == value_to_find):
            return index
    return -1

score = [88, 95, 70, 100, 99, 88, 78, 50]

print(f"학생수는 {len(score)}명 입니다.")
print(f"최고 점수는 {max(score)}점, {find_value(score, max(score))}번 학생입니다.")
print(f"최소 점수는 {min(score)}점, {find_value(score, min(score))}번 학생 입니다.")

print(f"99의 인덱스 : {find_value(score, 99)}")