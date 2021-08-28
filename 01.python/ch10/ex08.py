dic = { 'boy': '소년', 'school': '학교', 'book':'책' }
dic2 = { 'student': '학생', 'teacher': '선생님', 'book':'서적' }
dic.update(dic2)
print(dic)

# print(dic + dic2)


dic = { 'boy': '소년', 'school': '학교', 'book':'책' }
print(dic)

# dic3 = dict(dic)
dic3 = {}
dic3.update(dic)
dic3.update(dic2)

print(dic)
print(dic3


)
li = (
    ('boy', '소년'),
    ['school', '학교'],
    ['teacher', '선생님']
)
dic = dict(li)
print(dic)
print(type(li))
