import re
#regular expression
num_list = []

listA = []
listB = []
listC = []
similarityscore = 0


#not needed
with open("./D1Binput.txt", "r") as fh:
    for myline in fh: #file handling
        num_list.append(myline)
        numbers = re.findall(r'\d+', myline)
        #numbers = myline.split()
        listA.append(int(numbers[0]))
        listB.append(int(numbers[1]))

for i in listB:
    for j in listA:
        if i == j:
            listC.append(i)

same_numbers = set(listC)
for i in same_numbers:
    frequency = listC.count(i)
    similarityscore += i * frequency 


print (similarityscore)

#answer: 23981443


#dictionary data types - dictionaries
#Step 1: what numbers in listA appear in listB
#Step 2: how often numbers in listA appear in listB
#Step 3: multiply the numbers by how often they appear
#Step 4: add up the multiplied numbers


