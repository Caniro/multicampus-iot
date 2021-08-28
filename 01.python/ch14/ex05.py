try:
    with open("live.txt", "rt", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")

except Exception as e:
    print(e)
