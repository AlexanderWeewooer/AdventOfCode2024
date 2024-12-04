# PART 1 summing IDs

from pprint import pprint

#much needed lists
left= list()
right= list()
divided= list()

#for to get the lines from the input
with open("input.txt",'r') as file:
    for line in file:
        divided = line.split()
        if(len(divided)>=2 and divided[0]!="" and divided[1]!=""):
            left.append(int(divided[0].strip()))
            right.append(int(divided[1].strip()))

#now to the sorting
differences = list()
left.sort()
right.sort()

for l,r in zip(left,right):
    differences.append(abs(l-r))
print(differences)

#final sum
print(sum(differences))

# PART 2 Similarity score

new = list()

for l,r in zip(left,right):
    if(right.count(l)>0):
        new.append(right.count(l)*l)
    else:
        new.append(0)

print(sum(new))