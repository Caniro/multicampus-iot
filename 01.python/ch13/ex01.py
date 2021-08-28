scores = ["89", "89점"]

try:
    for score in scores:
        score_int = int(score)
        print(score_int)
except:
    print("예외가 발생했습니다.")
print("작업완료")
