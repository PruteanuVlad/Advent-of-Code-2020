f=open("Day 4 input.txt","r")
input=f.read()
passports=input.split("\n\n")

count=0

for x in passports:
    if x.find("byr")>-1 and x.find("iyr")>-1 and x.find("eyr")>-1 and x.find("hgt")>-1 and x.find("hcl")>-1 and x.find("ecl")>-1 and x.find("pid")>-1:
        count=count+1

print(count)