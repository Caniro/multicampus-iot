USER_ID = "hong"
PASSWORD = "abcd"

for _ in range(3):
    userid = input("아이디 입력 : ")
    password = input("비밀번호 입력 : ")

    if (userid != USER_ID or password != PASSWORD):
        print("아이디 또는 비밀번호가 일치하지 않습니다.")
    else:
        print("인증되었습니다.")
        break
