f=open("Day 1 input.txt","r")
list=[]
for line in f:
    list.append(int(line))
for i in range(0,len(list)-2):
    for j in range(i+1,len(list)-1):
        for k in range(j+1,len(list)):
            if list[i]+list[j]+list[k]==2020:
                print(list[i]*list[j]*list[k])
f.close()