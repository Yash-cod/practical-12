import mysql.connector as sql
mycon = sql.connect(host = "localhost", user = "root", passwd = "0001", database = "practical")
cur = mycon.cursor()
Query = "SELECT * FROM GRADUATE WHERE DEPT = 'CS'"
cur.execute(Query)
D = cur.fetchall()
print(D)
mycon.close()