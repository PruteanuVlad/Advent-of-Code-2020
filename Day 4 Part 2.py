f=open("Day 4 input.txt","r")
input=f.read()
passports=input.split("\n\n")

count=0

for x in passports:
    if x.find("byr")>-1 and x.find("iyr")>-1 and x.find("eyr")>-1 and x.find("hgt")>-1 and x.find("hcl")>-1 and x.find("ecl")>-1 and x.find("pid")>-1:
        i=x.find("byr")+4
        byr=0
        while i<len(x):
            if x[i].isdigit():
                byr=byr*10+int(x[i])
            else:
                break
            i=i+1
        if byr<=2002 and byr>=1920:
            i=x.find("iyr")+4
            iyr=0
            while i<len(x): 
                if x[i].isdigit():
                    iyr=iyr*10+int(x[i])
                else:
                    break
                i=i+1
            if iyr<=2020 and iyr>=2010:
                i=x.find("eyr")+4
                eyr=0
                while i<len(x):
                    if x[i].isdigit():
                        eyr=eyr*10+int(x[i])
                    else:
                        break
                    i=i+1
                if eyr<=2030 and eyr>=2020:
                    i=x.find("hgt")+4
                    hgt=0
                    while i<len(x):
                        if x[i].isdigit():
                            hgt=hgt*10+int(x[i])
                        else:
                            break
                        i=i+1
                    if (x[i]=='c' and hgt<=193 and hgt>=150) or (x[i]=='i' and hgt<=59 and hgt>=76 ):
                            count=count+1
                    

print(count)