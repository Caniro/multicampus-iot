dic = { 'boy': '소년', 'school': '학교', 'book':'책' }
print(dic.keys())
print(dic.values())

print()

print(dic.items())

print()

for key in dic.keys():
    print('key : ' + key + ', value : ' + dic[key])

print()

for item in dic.items():
    print('key : ' + item[0] + ', value : ' + item[1])

print()

for key, value in dic.items():
    print('key : ' + key + ', value : ' + value)

for x in dic:
    print(x)
