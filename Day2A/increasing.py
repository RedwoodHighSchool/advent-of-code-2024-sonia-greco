import re

sortlistasc = []
sortlistdes = []
safe = False
numsafe = 0 

with open("./D2Ainput.txt", "r") as fh:
    for myline in fh:
        numbers = re.findall(r'\d+', myline)
        numlist = [int(x) for x in numbers]
        sortlistasc = sorted(numlist)
        sortlistdec = sorted(numlist, reverse=True)
        if (sortlistasc == numlist) or (sortlistdec == numlist):
            for i in range(len(numlist) - 1):
                check = abs(numlist[i] - numlist[i + 1])
                if (check >= 1 and check <= 3):
                    safe += 1
            if (safe == len(numlist) - 1):
                numsafe += 1
            safe = 0
    print(numsafe)


    #answer: 516
                

               