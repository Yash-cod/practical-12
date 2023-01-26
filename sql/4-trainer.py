import mysql.connector as sql
mycon = sql.connect(host = "localhost", user = "root", passwd = "0001", database = "practical")
cur = mycon.cursor()
Query = "DELETE FROM TRAINER WHERE CITY = 'CHENNAI'"
cur.execute(Query)
mycon.commit()
print("TRAINER DETAILS ARE DELETED SUCCESSFULLY")
mycon.close()