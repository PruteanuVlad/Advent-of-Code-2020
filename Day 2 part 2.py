f=open("Day 2 input.txt","r")
list=[]
correct=0
for line in f:
    list.append((line))
for password in list:
    i=0
    pos1=0
    pos2=0
    ok=0
    while password[i].isdigit():
        pos1=pos1*10+int(password[i])
        i=i+1
    i=i+1
    while password[i].isdigit():
        pos2=pos2*10+int(password[i])
        i=i+1
    i=i+1
    c=password[i]
    i=i+2
    if (password[i+pos1]==c) != (password[i+pos2]==c):
        correct=correct+1
print(correct)
f.close()