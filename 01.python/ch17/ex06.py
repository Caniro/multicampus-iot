def makeHello(message):
    def hello(name):
        print(f"{message}, {name}")
    return hello

enghello = makeHello("Good Morning")
korhello = makeHello("안녕하세요")

print(enghello)
print(korhello)
print(id(enghello))
print(id(korhello))
print(id(makeHello))

enghello("Mr Kim")
korhello("홍길동")

li = [123, 124]
print(id(li))
