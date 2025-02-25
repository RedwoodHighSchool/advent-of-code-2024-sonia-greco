import re
#regular expression
num_list = []

listA = []
listB = []
similarityscore = 0



with open("./D1Binput.txt", "r") as fh:
    for myline in fh: #file handling
        num_list.append(myline)
        numbers = re.findall(r'\d+', myline)
        #numbers = myline.split()
        listA.append(int(numbers[0])) #not needed
        listB.append(int(numbers[1]))


#Multiply the numbers in listA by their occurrences in listB and then add all the results together

frequency_dict = {}

for i in listA:
    frequency_dict[i] = listB.count(i) #store values

for key, value in frequency_dict.items():
    similarityscore += key * value

print(similarityscore)
