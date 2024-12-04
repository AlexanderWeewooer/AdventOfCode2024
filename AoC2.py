# PART 1 safe levels

divided=list()
safe_reps=0 #safe reports counter

with open("input.txt",'r') as file:

    #taking all the lines and divinding them
    for line in file:
        buffer = line.split()
        divided = list(map(int, buffer))

        increasing = all( (divided[i] <= divided[i+1] ) for i in range( len(divided)-1 ))  #all incresing
        decreasing = all( (divided[i] >= divided[i+1] ) for i in range( len(divided)-1 ))  #all decreasing

        if(increasing or decreasing):
            safe = all(  1 <=   abs( divided[i] - divided[i+1] )  <= 3   for i in range( len(divided)-1 )) #at least 1 at most 3
            if(safe):
                safe_reps+=1
                print(divided)
                print("+1")

#final print of the counter
print(safe_reps)