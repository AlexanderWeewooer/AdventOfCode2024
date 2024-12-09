# PART 1 mul(n,n)
# there is only one thing that I hate more than Python. Python RegEx.

import re
muls = []
format = r"mul\(\d{1,3},\d{1,3}\)" #will never figure out a pattern again, yey
with open("input.txt",'r') as file:
    for line in file:
        match_format = re.findall(format,line,re.MULTILINE)
        muls.extend(match_format)

#print(muls)
pattern = r"\d{1,3}" #I was joking, I need another one
multiplied=0
for mul in muls:
    split = re.findall(pattern,mul)
    multiplied += (int(split[0]))*(int(split[1]))
print(multiplied)

#PART 2 but more

functions = []
format = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
do = r"do\(\)"
dont = r"don't\(\)"
with open("input.txt",'r') as file:
    for line in file:
        match_format = re.findall(format,line,re.MULTILINE)
        functions.extend(match_format)

#print(functions)
multiplied=0
switch=True
for fun in functions: #the fun I'm (not) having 
    if fun=="do()": switch=True
    elif fun=="don't()": switch=False
    else:
        if(switch):
            split = re.findall(pattern,fun)
            multiplied += (int(split[0]))*(int(split[1]))
print(multiplied)
#pattern = r"\d{1,3}"
