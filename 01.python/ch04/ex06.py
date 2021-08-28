# 문제 seconds 변수의 초 값을
# 분:초 로 출력하세요.

# seconds = 3150
# print(seconds // 60, seconds % 60, sep = ':')
# print('현재 시간 ', seconds // 60, ':', seconds % 60, sep = '')



ms = 123456789 # 밀리초
seconds = ms // 1000
minutes = (seconds // 60) % 60
# minutes = (seconds % 3600) // 60
hours = seconds // 3600
print(hours, ':', minutes, ':', 
  seconds % 60, '.', ms % 1000, sep = '')
