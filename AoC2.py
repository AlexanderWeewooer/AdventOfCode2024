# PART 1 safe levels

divided=list()
safe_reps=0 #safe reports counter

with open("input.txt",'r') as file:

    #taking all the lines and divinding them
    for line in file:
        buffer = line.split()
        divided = list(map(int, buffer))

        increasing = all( (divided[i] <= divided[i+1] ) for i in range( len(divided)-1 )  )  #all incresing
        decreasing = all( (divided[i] >= divided[i+1] ) for i in range( len(divided)-1 )  )  #all decreasing

        if(increasing or decreasing):
            safe = all(  1 <=   abs( divided[i] - divided[i+1] )  <= 3   for i in range( len(divided)-1 )  ) #at least 1 at most 3
            if(safe):
                safe_reps+=1
                print(divided)
                print("+1")

#final print of the counter
print(safe_reps)


# PART 2 tolerance

divided=list()
safe_reps=0 #safe reports counter
flag=0

with open("input.txt",'r') as file:

    flag=0
    #taking all the lines and divinding them
    for line in file:
        buffer = line.split()
        divided = list(map(int, buffer))
        
        #all increasing --------------------------------
        increasing = False 
        count=0
        while(  count in range(len(divided)-1)  ):
            if(divided[count] <= divided[count+1]):
                count+=1
            else:
                flag+=1
                count+=1

        #if one element is wrong it still works
        if(flag>1):
            increasing = False
        else:
            increasing = True
        
        #all decreasing -------------------------------
        decreasing = False 
        flag=0 #resetting flag for controls
        count=0
        while(  count in range(len(divided)-1)  ):
            if(divided[count] >= divided[count+1]):
                count+=1
            else:
                flag+=1
                count+=1

        #if one element is wrong it still works
        if(flag>1):
            decreasing = False
        else:
            decreasing = True

        #between 1 and 3 ------------------------------------
        count=0
        if(increasing or decreasing):
            safe = 0
            while( count in range(len(divided)-1) ):
                if(1 <= abs( divided[count] - divided[count+1] )<= 3 ): 
                    count+=1
                else:
                    count+=1
                    safe+=1

        if(safe<=1):
            safe_reps+=1
            print(divided)
            print("+1")

#final print of the counter
print(safe_reps)