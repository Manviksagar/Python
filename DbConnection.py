import pymysql

# database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="sag")
cursor = connection.cursor()
retrive = "Select * from sag_ta;"

# executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
