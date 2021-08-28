import sqlite3

with sqlite3.connect("addr.db") as con:
    cursor = con.cursor()
    sql = "SELECT * FROM tblAddr order by addr"
    cursor.execute(sql)
    table = cursor.fetchall() # sql문의 결과인 행이 담긴 전체 리스트를 리턴한다. 없으면 []
    for name, phone, address in table:
        print(f"이름: {name}, 전화: {phone}, 주소: {address}")
    print()

    cursor.execute(sql)
    table = cursor.fetchmany(2) # 지정한 수만큼 리스트로 리턴한다.
    for name, phone, address in table:
        print(f"이름: {name}, 전화: {phone}, 주소: {address}")
    print()

    table = cursor.fetchmany(2)
    for name, phone, address in table:
        print(f"이름: {name}, 전화: {phone}, 주소: {address}")
    print()

    cursor.execute(sql)
    table = cursor.fetchone()
    name, phone, address = table
    print(f"이름: {name}, 전화: {phone}, 주소: {address}")

    cursor.close()
