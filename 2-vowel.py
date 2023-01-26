file = open("C:\\Users\\user\\OneDrive\\programs\\#github\\practical-12\\files\\story.txt")
read = file.read()
v = ["a","A","e","E","i","I","o","O","u","U"]
vcount=0
ccount=0
read = "".join(read.split())
for i in read:
    if i in v:
        vcount+=1
    else:
        ccount+=1
ucount=0
lcount=0
for i in read:
    if i.isupper():
        ucount+=1
    else:
        lcount+=1

print("NUMBER OF VOWELS  FOUND IS : ",vcount)
print("NUMBER OF CONSONANT FOUND IS : ",ccount)
print("NUMBER OF UPPERCASE LETTERS IS : ",ucount)
print("NUMBER OF LOWERCASE LETTERS IS : ",lcount)

