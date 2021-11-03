# 문자열 슬라이싱

file = "20200101-104830.jpg"
print("촬영 년도 : " + file[:4] + "년")
print("촬영 날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영 시간 : " + file[9:11] + "시 " + file[11:13] + "분 " + file[13:15] + "초")
print("확장자 : " + file[-3:])

dates = "월화수목금토일"
print(dates[::2])  # step 지정
print(dates[::-1]) # 거꾸로
print(dates[-1::])

''' stdout
촬영 년도 : 2020년
촬영 날짜 : 01월 01일
촬영 시간 : 10시 48분 30초
확장자 : jpg
월수금일
일토금목수화월
일
'''
