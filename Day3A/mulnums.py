import re

mul_list = []

with open("./D3Ainput.txt", "r") as fh:
    for myline in fh:
       #mul_list.append(myline)
        numbers = re.findall(r'mul\d', myline)
        print (num)