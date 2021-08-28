with open("live.txt", "rt", encoding="UTF-8") as f:
    f.seek(12, 0)
    text = f.read() # 예외 발생
    print(text)
