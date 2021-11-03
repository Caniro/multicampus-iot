# 문자열 슬라이싱

s = "0123456789"
print(s[2:5])
print(s[3:])
print(s[:4])

# 파일이 mp3 확장자인지 확인
file_name = "song.mp3"
if (file_name[-4:] == ".mp3"):
    print("mp3 파일입니다.")
else:
    print("mp3 파일이 아닙니다.")

# 연월일 분리
s_num = "900302"
print("출생년도 :", s_num[:2])
print("출생월:", s_num[2:4])
print("출생일:", s_num[4:])

''' stdout
234
3456789
0123
mp3 파일입니다.
출생년도 : 90
출생월: 03
출생일: 02
'''
