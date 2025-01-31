import re


safe = False
numsafe = 0 
unsafelevel = 0

def checklvl(testlist, unsafelevelindex, infractions):
    safe = 0
    sortlistasc = []
    sortlistdes = []
    sortlistasc = sorted(testlist)
    sortlistdes = sorted(testlist, reverse=True)

    if (sortlistasc == testlist) or (sortlistdes == testlist):
        for i in range(len(testlist) - 1):
            check = abs(testlist[i] - testlist[i + 1])
            if (1 <= check <= 3):
                safe += 1
            else:
                infractions += 1    
                unsafelevelindex = i

        if safe == len(testlist) - 1:
            return True
        else:
            return False

with open("./D2Binput.txt", "r") as fh:
    for myline in fh:
        numbers = re.findall(r'\d+', myline)
        numlist = [int(x) for x in numbers]
        unsafelevelindex = 0
        infractions = 0
        if (checklvl(numlist, unsafelevelindex, infractions)):
            numsafe += 1
        else:
            if infractions == 1:
                numlist.remove(unsafelevelindex)
            
            #remove the element which is at index unsafelevel and call function again
         
         #count all the infraction per level. If there are more than 1 then it is unsafe
                #get the index of the list which is not safe and assign it to level
                #also need a flag to indicate that this is done only once

with open("./D2Binput.txt", "r") as fh:
    for myline in fh:
        numbers = re.findall(r'\d+', myline)
        numlist = [int(x) for x in numbers]
        if (checklvl(numlist, unsafelvl)):
            numsafe += 1
        else:
            numlist.pop(i, unsafelvl)
            unsafelvl -= 1
         
         
"""
for i in range(len(numlist) - 1):
    templist = numlist[:i] + numlist[i+1:]
    if templist == sorted(templist) or templist == sorted(templist, reverse=True):
        safe = True
    for j in range(len(templist) - 1):
        check = abs(templist[j] - templist[j + 1])
        if (1 <= check <= 3):  # If the difference isn't valid
            safe += 1
    if (safe == len(numlist) - 1):
        numsafe += 1
    safe = 0
"""
#if sortlist == numlist or sortlist - i == numlist

print(numsafe)