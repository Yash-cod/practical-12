def fac(no):
   p = len(no)
   for i in range (0,p):
      if no[i] < 0:
         print("FACTORIAL OF A NEGATIVE NO DOES NOT EXISTS")
      elif no[i] == 0:
         print("FACTORIAL OF 0 IS 1")
      else:
         f = 1
         for j in range(1,no[i]+1):
            f = f*j
         print("THE FACTORIAL OF ", no[i], " IS ", f)
      
def sum(no):
   p = len(no)-1
   k = 0
   for i in range (0, len(no)):
      k = k+no[i]
   print("SUM OF THE NO IN LIST : ", k)

while True:
   print("1. FACTORIAL OF LIST OF NUMBERS")
   print("2. SUM OF LIST OF NUMBERS")
   print("3. EXIT THE SYSTEM")

   ch = int(input("ENTER ACTION : "))
   if ch == 1:
      no = eval(input("ENTER A NUMBER : "))
      no = list(no)
      fac(no)
   elif ch == 2:
      no = eval(input("ENTER A NUMBER : "))
      no = list(no)
      sum(no)
   else:
      break