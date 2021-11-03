# 문자열 함수

s = "Good morning. my love KIM."
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())

s = " angel "
print(s + "님")
print(s.strip() + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")

''' stdout
good morning. my love kim.
GOOD MORNING. MY LOVE KIM.
gOOD MORNING. MY LOVE kim.
Good morning. my love kim.
Good Morning. My Love Kim.
 angel 님
angel님
angel 님
 angel님
'''
