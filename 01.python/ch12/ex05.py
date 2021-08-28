from datetime import datetime
now = datetime.now()
days = ("월", "화", "수", "목", "금", "토", "일")
print(f"{now.year}년 {now.month}월 {now.day}일 {days[now.weekday()]}요일", end = ' ')
print(f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")
