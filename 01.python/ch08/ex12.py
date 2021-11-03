# 문자열 함수

trabler = """\
강나루 거너서
밀밭 길을

구름에 달 가듯이
가는 나그네
"""
poet = trabler.splitlines()
print(poet)
for line in poet:
    print(line)

s ="._."
print(s.join("대한민국"))

# s = "독도는 일본땅. 대마도도 일본땅"
# print(s)
# print(s.replace("일본", "한국"))

trabler ="""\
강나루 거너서
밀밭 길을
구름에 달 가듯이
가는 나그네
"""
poet = trabler.splitlines()
for line in poet:
    print(line.center(30))

''' stdout
['강나루 거너서', '밀밭 길을', '', '구름에 달 가듯이', '가는 나그네']
강나루 거너서
밀밭 길을

구름에 달 가듯이
가는 나그네
대._.한._.민._.국
           강나루 거너서            
            밀밭 길을             
          구름에 달 가듯이           
            가는 나그네 
'''
