try:
    with open("live.txt", "rt", encoding="UTF-8") as f:
        rows = f.readlines()
        print(type(rows))
        for row in rows:
            print(row, end="")

except Exception as e:
    print(e)
