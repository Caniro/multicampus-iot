# ---- 요구 사항 예시 ----
# 파일 목록
# 1) addressbook copy.txt
# 2) addressbook.txt
# 3) live.txt
# 4) live2.txt
# 5) memo.txt
#
# 파일 선택 : 3
# live.txt 내용을 출력
#
# 파일 선택 : -1
# 종료
# -----------------------

import os

def get_files(dir_path, ext):
    return [fname for fname in os.listdir(dir_path) if fname.endswith(ext)]


def print_file_list(files):
    print("\n\n--- 파일 목록 ---")
    for idx, fname in enumerate(files, 1):
        print(f"{idx}) {fname}")
    print()


def print_file(file_name):
    try:
        with open(file_name, "rt", encoding="UTF-8") as f:
            text = f.read()
            print(text)
    except Exception as e:
        print(e)


while (True):
    txt_list = get_files('.', '.txt')
    print_file_list(txt_list)
    selected_no = int(input("파일을 선택하세요 : "))
    if (selected_no == -1):
        print("종료합니다.")
        break
    print_file(txt_list[selected_no - 1])
