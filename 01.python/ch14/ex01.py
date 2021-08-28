# f = open("live.txt", "wt", encoding="UTF-8")

# f.write("""삶이 그대를 속일지라도
# 슬퍼하거나 노하지 말라!
# 우울한 날들을 견디면
# 믿으라, 기쁨의 날이 오리니""")
# f.write("\n추가1")
# f.write("\n추가2")
# f.write("\n추가3")

# f.close()

try:
    with open("live.txt", "wt", encoding="UTF-8") as f:
        f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
except Exception as e:
    print(e)
