import mysql.connector as sql
mycon = sql.connect(host="localhost", user = "root", passwd = "0001", database = "practical")
cur = mycon.cursor()
Q = "UPDATE BOOKS SET PRICE = PRICE + (PRICE*0.1) WHERE PRICE > 300"
cur.execute(Q)
mycon.commit()
mycon.close()
print("BOOK DETAILS ARE UPDATED SUCCESSFULLY")