# 조건문 안의 조건문

man = True
age = 22
if man == True:
    if age > 19:
        print("성인 남자입니다.")
    else:
        print("미성년 남자입니다.")
else:
    if age > 19:
        print("성인 여자입니다.")
    else:
        print("미성년 여자입니다.")

''' stdout
성인 남자입니다.
'''
