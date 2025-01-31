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