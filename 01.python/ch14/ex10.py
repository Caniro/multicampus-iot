# import os
# from pprint import pprint

# files = os.listdir('.')
# cwd = os.getcwd()
# print(f"cwd : {cwd}")

# for f in files:
#     fpath = os.path.join(cwd, f)
#     if os.path.isfile(f):
#         temp = []
#         temp.append(fpath)
#         print(fpath) # 출력해보면 구분자가 '\'인데 내부적으로는 문자열 "\\"로 저장된 듯?
#         print(temp)
#         f = open(fpath, "rt", encoding="UTF-8")
#         print(f.seek(0, 2))
#         f.close()
    # if os.path.isdir(fpath):
    #     print(f"<dir> {fpath}")
    # else:
    #     print(fpath)

import os
from pprint import pprint

# 지정한 확장명을 가지는 파일명 목록을 리턴하는 함수
def get_files(dir_path, ext):
    files = os.listdir(dir_path)
    cwd = os.getcwd()
    print(f"cwd : {cwd}")

    # # 0. 일반 순회
    # file_list = []
    # for f in files:
    #     fpath = os.path.join(cwd, f)
    #     print(fpath)
    #     if (os.path.isfile(fpath)) and (fpath.endswith(ext)):
    #         file_list.append(fpath)
    # return file_list

    # # 1. filter 함수 적용 
    # files = map(lambda fname: os.path.join(cwd, fname), files)
    # file_list = list(filter(lambda fname: fname.endswith(ext), files))
    # return file_list

    # 2. 컴프리헨션
    return [os.path.join(cwd, fname) for fname in files if fname.endswith(ext)]


file_list = get_files('.', '.txt')
pprint(file_list)
