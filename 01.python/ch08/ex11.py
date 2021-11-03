# 문자열 함수

s = "짜장  짬뽕  탕수육"
print(s.split())
print(s.split(' '))

s2 = "서울->대전->대구->부산"
cities = s2.split("->")
print(cities)
for city in cities:
    print(city)

file_path = "\\temp\\test_a\\a.txt"
# print(file_path.split('\\')[-1])
# print(file_path.split('.')[-1])

dirs = file_path.split('\\')[:-1]
print(dirs)
dir_path = '\\'.join(dirs)
print(dir_path)

s = "백반 "
print(s.split())

s = "백반,"
print(s.split(','))

data = "10, 60.4, 700"
data_list = data.split(',')
print(data_list)

''' stdout
['짜장', '짬뽕', '탕수육']
['짜장', '', '짬뽕', '', '탕수육']
['서울', '대전', '대구', '부산']
서울
대전
대구
부산
['', 'temp', 'test_a']
\temp\test_a
['백반']
['백반', '']
['10', ' 60.4', ' 700']
'''
