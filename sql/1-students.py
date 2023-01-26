import mysql.connector as sql
con1 = sql.connect(host="localhost", user = "root",
passwd = "0001", database = "practical")
mycursor = con1.cursor()
print("STUDENTS WITH PERCENTAGE GREATER THAN 75 ARE : ")
mycursor.execute("SELECT * FROM STUDENTS WHERE PERCENTAGE > 75")
data = mycursor.fetchall()
for i in data:
   print(i)
   print()

con1.close()