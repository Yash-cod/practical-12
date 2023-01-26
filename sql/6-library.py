import mysql.connector as sql
mycon = sql.connect(host = "localhost", user = "root", passwd = "0001", database = "practical")
cur = mycon.cursor()
Q = "SELECT * FROM LIBRARY WHERE PRICE IS NULL AND QTY > 15"
cur.execute(Q)
D = cur.fetchall()
print(D)
mycon.close()