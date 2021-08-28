# 키를 무지개 색인 빨, 주, 노, 초, 파, 남, 보로 하고
# 값을 각 색상의 영어 단어로 정의한 후
# 초록색의 영어 단어를 검색하는 예제를 작성하라.

colors = {
    "빨": "red",
    "주": "orange",
    "노": "yellow", 
    "초": "green", 
    "파": "blue", 
    "남": "indigo", 
    "보": "purple"
}

color_green = colors.get('초')
if (color_green):
    print(f"초록색 : {color_green}")
else:
    print("초록색이 사전에 없음")
