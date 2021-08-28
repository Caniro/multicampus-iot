# sosi 문자열에 "태연, 서연, 수영" 이름이 저장되어 있다.
# 각 가수의 이름을 추출하여 "사랑해"와 함께 출력하라.

sosi = "태연, 서연, 수영"
sosi_list = sosi.split(", ")

for name in sosi_list:
    print(f"{name} 사랑해")
