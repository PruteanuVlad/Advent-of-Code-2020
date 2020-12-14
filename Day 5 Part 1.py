import math
f=open("Day 5 input.txt","r")
input=f.read()
passes=input.split("\n")
max=0
for x in passes:
    lc=0
    hc=127
    lr=0
    hr=7
    id=0
    for i in range(8):
        if x[i]=='F':
            hc=lc+math.floor((hc-lc)/2)
        if x[i]=='B':
            lc=lc+math.ceil((hc-lc)/2) 
    for i in range(7,10):
        if x[i]=='L':
            hr=lr+math.floor((hr-lr)/2)
        if x[i]=='R':
            lr=lr+math.ceil((hr-lr)/2) 
    id=hc*8+hr
    if id>max:
        max=id
print(max)