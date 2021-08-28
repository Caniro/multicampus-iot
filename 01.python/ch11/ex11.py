def test():
    list1 = [1, 2, 3]
    print(list1)
    print(id(list1))
    return list1

def test2(l2):
    l2[0] = 100
    print(f"l2 : {l2}")

li = test()
print(li)
print(id(li))
test2(li)
print(li)
