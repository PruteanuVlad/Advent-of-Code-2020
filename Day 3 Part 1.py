import numpy as np
np.set_printoptions(threshold=np.inf)

map=np.zeros( (323,31 ) )
trees=0 

f=open("Day 3 input.txt","r")
list=[]
for line in f:
    list.append((line))

i=0
j=0
for line in list:
    j=0
    for x in line:
        if x=='#':
            map[i][j]=1
        j=j+1
    i=i+1

i=i-1
j=j-1

m=1
n=3

while m<i+1:
    if map[m][n%31]==1:
        trees=trees+1
    m=m+1
    n=n+3
print(trees)
