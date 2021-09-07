# import MySQLdb

# username = "root"
# password = ""
# db = MySQLdb.connect(host="localhost", user=username, \
#     passwd=password, db="employees")
# with db:
#     cur = db.cursor()

#     sql = "SELECT * FROM employees"
#     cur.execute(sql)
#     table = cur.fetchmany(10)

#     for record in table:
#         print(record)

#     cur.close()


import MySQLdb

username = "iot"
password = "1234"
db = MySQLdb.connect(host="localhost", user=username, \
    passwd=password, db="employees")
with db:
    cur = db.cursor()

    sql = "SELECT * FROM employees"
    cur.execute(sql)
    table = cur.fetchmany(10)

    for record in table:
        print(record)

    cur.close()
