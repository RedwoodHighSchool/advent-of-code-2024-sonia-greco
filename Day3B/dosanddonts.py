import re

total = 0
enabled = True

with open("./D3Binput.txt", "r") as fh:
    myline = fh.read().strip()
"""
match = re.findall(r"don't|do|mul\((\d+)?,(\d+)?\)", myline)
for i in match:
#   print (i)
    if i.group(0) == "do":
        enabled = True
    elif i.group(0) == "don't":
        enabled = False
    elif i.group(0) == enabled:
        total += int(i[1]) * int(i[2])
"""
for match in re.finditer(r"don't|do|mul\((\d+)?,(\d+)?\)", myline):
    if match.group(0) == "do":
        enabled = True
    elif match.group(0) == "don't":
        enabled = False
    elif enabled:
        total += int(match.group(1)) * int(match.group(2))

print (total)