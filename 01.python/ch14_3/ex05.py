import sqlite3

with sqlite3.connect("addr.db") as con:
    cursor = con.cursor()
    # sql = "UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'"
    sql = "DELETE FROM tblAddr WHERE name = '김상형'"
    cursor.execute(sql)
    con.commit()
    cursor.close()
