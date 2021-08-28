file = "20200101-104830.jpg"
print("촬영 년도 : " + file[:4] + "년")
print("촬영 날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영 시간 : " + file[9:11] + "시 " + file[11:13] + "분 " + file[13:15] + "초")
print("확장자 : " + file[-3:])

dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])
print(dates[-1::])

