# import sqlite3

# with sqlite3.connect("addr.db") as con:
#     cursor = con.cursor()
#     sql = "SELECT addr FROM tblAddr where name = '김상형'"
#     cursor.execute(sql)
#     record = cursor.fetchone() # Primary Key로 where 절을 구성한 경우 행이 1개이거나 없으므로 이걸 많이 사용한다.
#     if record: print(f"김상형은 {record[0]}에 살고 있습니다.")
#     else: print("김상형은 없는 이름입니다.")

#     cursor.close()

# 검색할 이름을 사용자로부터 입력받아서 처리
import sqlite3

with sqlite3.connect("addr.db") as con:
    cursor = con.cursor()
    name = input("이름을 입력하세요 : ")
    sql = f"SELECT addr FROM tblAddr where name = '{name}'"
    cursor.execute(sql)
    record = cursor.fetchone()
    if record: print(f"{name}은 {record[0]}에 살고 있습니다.")
    else: print(f"{name}은 없는 이름입니다.")

    cursor.close()
