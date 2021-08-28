try:
    with open("live.txt", "rt", encoding="UTF-8") as f:
        text = ""
        line = 1

        while True:
            row = f.readline()
            if not row: break
            text += f"{line} : {row}"
            line += 1
        print(text)
except Exception as e:
    print(e)
