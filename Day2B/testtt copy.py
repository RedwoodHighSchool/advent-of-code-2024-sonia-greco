import re

sortlistasc = []
sortlistdes = []
numsafe = 0

def checklvl(testlist):
    safe = 0
    unsafelvl = 0
    sortlistasc = sorted(testlist)
    sortlistdec = sorted(testlist, reverse=True)

    if (sortlistasc == testlist) or (sortlistdec == testlist):
        for i in range(len(testlist) - 1):
            check = abs(testlist[i] - testlist[i + 1])
            if (1 <= check <= 3):
                safe += 1
            else:
                unsafelvl += 1

    if unsafelvl <= 1:
        return True
    else:
        return False

with open("./D2Binput.txt", "r") as fh:
    numsafe = 0
    for myline in fh:
        numbers = re.findall(r'\d+', myline)
        numlist = [int(x) for x in numbers]

        if  (checklvl(numlist)):
            print(numlist)
            print(numsafe)
            numsafe += 1  
print(numsafe)


    #answer: 561