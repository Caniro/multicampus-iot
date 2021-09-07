import sqlite3

with sqlite3.connect("addr.db") as con:
    cursor = con.cursor()
    sql = "SELECT * FROM tblAddr order by addr"
    cursor.execute(sql)
    while True:
        record = cursor.fetchone()
        if record == None: break
        name, phone, address = record
        print(f"이름: {name}, 전화: {phone}, 주소: {address}")

    cursor.close()
