list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
list1.extend(list2)
print(list1)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list3 = list1 + list2 # 새로운 리스트를 리턴
print(list1)
print(list3)
list1.extend(list2) # 기존 리스트를 확장
print(list1)