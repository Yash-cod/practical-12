def empty(stk):
    if stk == []:
        return True
    else:
        return False

def push(stk,name):
    stk.append(name)
    top = len(stk)-1

def pop(stk):
    if empty(stk):
        return "UNDERFLOW"
    else:
        name = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return name

def peek(stk):
    if empty(stk):
        return "UNDERFLOW"
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if empty(stk):
        print("STACK EMPTY")
    else:
        top=len(stk)-1
        print(stk[top], "<--top")
        for a in range(top-1,-1,-1):
            print(stk[a])

stk=[]
top=None
while True:
   print("MAIN MENU")
   print("1. INSERT NAME")
   print("2. DELETE NAME")
   print("3. PEEK NAME")
   print("4. DISPLAY STACK ")
   print("5. EXIT")
   ch=int(input("ENTER ACTION : "))

   if ch==1:
      name=input("ENTER STUDENT NAME : ")
      push(stk,name)

   elif ch==2:
      name=pop(stk)
      if name=="UNDERFLOW":
         print("UNDERFLOW! STACK IS EMPTY")
      else:
         print("POPPED NAME",name)

   elif ch==3:
      name=peek(stk)
      if name=="UNDERFLOW":
         print("UNDERFLOW!STACK IS EMPTY")
      else:
         print("TOPMOST NAME",name)

   elif ch==4:
      display(stk)

   elif ch==5:
      break
