f=open("Day 2 input.txt","r")
list=[]
correct=0
for line in f:
    list.append((line))
for password in list:
    i=0
    min=0
    max=0
    count=0
    while password[i].isdigit():
        min=min*10+int(password[i])
        i=i+1
    i=i+1
    while password[i].isdigit():
        max=max*10+int(password[i])
        i=i+1
    i=i+1
    c=password[i]
    i=i+3
    for j in range(i, len(password)):
        if password[j]==c:
            count=count+1
        i=i+1
    if count>=min and count<=max:
        correct=correct+1
print(correct)
f.close()