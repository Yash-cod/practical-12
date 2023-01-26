def counter():
   file = open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\ABC.txt","r+")
   count = 0
   data = file.read()
   text = data.split()
   for i in text :
      if i == 'Me' or i == 'My':
         count = count + 1
   print("COUNT : ",count)
   file.close()
    
def read():
   file = open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\MyNotes.txt","r")
   while True:
      line = file.readline()
      if line[0:1] in ("a", "m"):
         print(line)

while True:
   print("MAIN MENU")
   print("1. COUNT 'ME' AND 'MY'")
   print("2. DISPLAY LINES STARTING FROM 'A', 'M'")
   print("3. EXIT THE SYSTEM")
   ch = int(input("ENTER ACTION : "))
   if ch == 1:
      counter()
   elif ch == 2:
      read()
   else:
      break



