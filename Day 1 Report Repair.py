f=open("Day 1 Report Repair input.txt","r")
list=[]
for line in f:
    list.append(int(line))
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==2020:
            print(list[i]*list[j])
f.close()