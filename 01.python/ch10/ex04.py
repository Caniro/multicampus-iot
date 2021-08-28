users = {
    'kim': '1234',
    'hong': '12',
    'lee': 'abc'
}

user_id = input('user id : ')
password = input('password : ')

# if (users.get(user_id) and password == users.get(user_id)):
if (user_id in users) and (password == users.get(user_id)):
    print(f"Hello {user_id}!")
else:
    print("아이디 혹은 비밀번호가 일치하지 않습니다.")
