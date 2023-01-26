import csv
def read():
      with open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\employee.csv", mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                  print(row[0], row[1], row[2])

def write():
      with open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\employee.csv", mode = 'a', newline='') as file:
            writer = csv.writer(file,delimiter=',')
            ch = 'y'
            while ch.lower() == 'y':
                  eno = int(input("ENTER EMPLOYEE NUMBER : "))
                  name = input("ENTER EMPLOYEE NAME : ")
                  salary = int(input("ENTER EMPLOYEE SALARY : "))
                  writer.writerow([eno,name,salary])
                  print("DATA SUCCESSFULLY RECORDED!")
                  ch = input("DO YOU WANT TO ADD MORE RECORDS? Y/N : ")

def search():
      with open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\employee.csv", mode = 'r') as file:
            read = csv.reader(file)
            ans = 'y'
            while ans.lower() == 'y':
                  found = False
                  search = int(input("ENTER EMPLOYEE NUMBER TO SEARCH : "))
                  for row in read:
                        if len(row) !=0:
                              if int(row[0]) == search:
                                    print("EMPLOYEE NAME : ", row[1])
                                    print("EMPLOYEE SALARY : ", row[2])
                                    found = True
                                    break
                        elif not found:
                              print("EMPLOYEE RECORD NOT FOUND.")
                  ans = input("DO YOU WANT TO SEARCH AGAIN? Y/N : ")

def mainmenu():
    print("______________________________________________")
    print("1. READING FROM CSV FILE")
    print("2. WRITING DATA TO CSV FILE")
    print("3. SEARCHING ANY EMPLOYEE NO")
    print("4. EXIT")
    print("______________________________________________")

while True:
    mainmenu()
    ch = int(input("ENTER ACTION : "))
    if ch == 1:
        read()
    elif ch == 2:
        write()
    elif ch == 3:
        search()
    elif ch == 4:
        break