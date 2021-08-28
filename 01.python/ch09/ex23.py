names = "이순신", "김유신", "강감찬"
(lee, kim, kang) = names # unpack
print(lee)
print(kim)
print(kang)
print(lee, kim, kang)

(lee, kim, kang) = reversed(names) # unpack
print(lee, kim, kang)

print(type((lee, kim, kang)))

a = 10
b = 20
c = 30
tu = (a, b, c)
tu = (40, 50, 60)
print(tu)
