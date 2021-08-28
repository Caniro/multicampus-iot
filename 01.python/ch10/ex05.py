dic = { 'boy': '소년', 'school': '학교', 'book':'책'}
dic['boy'] = '남자아이' # key가 존재하면 수정
dic['girl'] = '소녀' # 키가 존재하지 않으면 추가
del dic['book'] # 기존 키에 해당하는 element 삭제
print(dic)

del dic['???'] # 키가 없으므로 에러
