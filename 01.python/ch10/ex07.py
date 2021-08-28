dic = {
    'boy': '소년',
    'school': '학교',
    'book':'책'
}

key_list = list(dic.keys())
key_list.sort()
for key in key_list:
    print(dic[key])

print(list(dic))
