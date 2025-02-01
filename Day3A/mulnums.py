import re

mul_list = []
mulled = 0
numbers = [] 

with open("./D3Ainput.txt", "r") as fh:
    myline = fh.read().strip()

numbers = re.findall(r"mul\((\d+),(\d+)\)", myline)
print (numbers)

for i in numbers:
    mulled += int(i[0]) * int(i[1])

print (mulled)

#answer: 188192787