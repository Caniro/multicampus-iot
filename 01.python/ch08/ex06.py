# 문자열 함수

s = "python programming"
print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

file_name = "test.jpeg"
# idx = file_name.index(".")
# idx = file_name.rfind(".")
# if (idx != -1):
#     extension = file_name[idx + 1:]
#     print(extension)

def print_file_ext(fname):
    idx = fname.rfind(".")
    if (idx != -1):
        extension = fname[idx + 1:]
        print(extension)

print_file_ext(file_name)

''' stdout
18
4
9
8
2
jpeg
'''
