f = open("live.txt", "at", encoding="UTF-8")
f.write("\n\n푸쉬킨 형님의 말씀")
print(type(f.tell()))
f.close()
