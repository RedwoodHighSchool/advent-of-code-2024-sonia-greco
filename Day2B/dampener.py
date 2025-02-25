def is_safe(level):
    safe = 0
    sortlistasc = []
    sortlistdes = []
    sortlistasc = sorted(level)
    sortlistdes = sorted(level, reverse=True)

    if (sortlistasc == level) or (sortlistdes == level):
        for i in range(len(level) - 1):
            check = abs(level[i] - level[i + 1])
            if (1 <= check <= 3):
                safe += 1
        if safe == len(level) - 1:
            return True
        else:
            return False

def is_safe_with_removal(level):
    for i in range(len(level)):
        modified_report = level[:i] + level[i + 1:]
        if is_safe(modified_report):
            return True
    return False

reports = []
with open("./D2Binput.txt", 'r') as f:
    for line in f:
        reports.append([int(x) for x in line.strip().split()])

safe_reports = 0
safe_with_removal = 0

for report in reports:
    print (report)
    if is_safe(report):
        safe_reports += 1
    if is_safe_with_removal(report):
        safe_with_removal += 1

print("Part 1:", safe_reports)
print("Part 2:", safe_with_removal)