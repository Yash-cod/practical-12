import pickle
def add():
   file = open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\students.dat", "wb")
   print("ADDING NEW RECORDS")
   record = []
   while True:
      rn = int(input("ENTER STUDENT ROLL NO : "))
      name = input("ENTER STUDENT NAME : ")
      marks = int(input("ENTER STUDENT MARKS : "))
      data = [rn, name, marks]
      record.append(data)
      ch = input("ADD MORE RECORDS? Y/N : ")
      if ch in  'Nn' :
         break
   pickle.dump(record,file)
   print("ADDED NEW RECORDS")
   file.close()

def search():
   file = open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\students.dat", "rb")
   data = pickle.load(file)
   found = 0
   print("SEARCHING FOR RECORDS")
   rn = int(input("ENTER THE ROLL NO TO BE SEARCHED : "))
   for i in data:
      if rn == i[0]:
         print("RECORD FOUND")
         print("STUDENT NAME : ",i[1])
         print("MARKS : ", i[2])
         found = 1
   if found == 0:
      print("NO RECORDS FOUND")
   file.close()

while True:
   print("MAIN MENU")
   print("1. INSERT RECORDS")
   print("2. SEARCH RECORDS")
   print("3. EXIT SYSTEM")
   ch = int(input("ENTER ACTION : "))
   if ch == 1:
      add()
   elif ch == 2:
      search()
   else:
      break