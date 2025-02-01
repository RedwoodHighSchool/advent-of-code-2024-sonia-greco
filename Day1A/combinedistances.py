import re

num_list = []

listA = []
listB = []
sumofdiff = 0

with open("./D1Ainput.txt", "r") as fh:
    for myline in fh:
        num_list.append(myline)
        numbers = re.findall(r'\d+', myline)
        #numbers = myline.split()
        listA.append(int(numbers[0]))
        listB.append(int(numbers[1]))

listA.sort()
listB.sort()

listlen = len(listA)

for i in range(listlen):
    sumofdiff += abs(listA[i] - listB[i])

print (sumofdiff)

#answer = 1258579