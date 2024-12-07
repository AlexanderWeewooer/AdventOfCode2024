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


# PART 2 tolerance (my tolerance to PYTHON GODDAMNIT)
# I found out I am stupid: I completely, We completely (I asked other students), Forgot the literal fundamental mechanich of this level.
# I have to remove one element at the time and THEN CHECK.

divided = list()
safe_reps = 0  # safe reports counter

with open("input.txt", 'r') as file:
    for line in file:
        safe = False
        buffer = line.split()
        buffer[0].replace("ï»¿",'')
        print(buffer)
        if buffer[0].isdigit():
            divided = list(map(int, buffer))

            increasing = all(divided[i] <= divided[i + 1] for i in range(len(divided) - 1)) #all increasing
            decreasing = all(divided[i] >= divided[i + 1] for i in range(len(divided) - 1)) #all decreasing

            if increasing or decreasing:
                safe = all(1 <= abs(divided[i] - divided[i + 1]) <= 3 for i in range(len(divided) - 1)) #within range

            if safe:
                safe_reps += 1
                continue

            #piece of code I wish I thought of three days ago
            for i in range(len(divided)):
                modified_report = divided[:i] + divided[i + 1:]

                modified_increasing = all(modified_report[j] <= modified_report[j + 1] for j in range(len(modified_report) - 1))
                modified_decreasing = all(modified_report[j] >= modified_report[j + 1] for j in range(len(modified_report) - 1))
                modified_distances = all(1 <= abs(modified_report[j] - modified_report[j + 1]) <= 3 for j in range(len(modified_report) - 1))

                if (modified_increasing or modified_decreasing) and modified_distances:
                    safe = True
                    break
            if safe:
                safe_reps += 1

print(f"Total safe reports: {safe_reps}")
