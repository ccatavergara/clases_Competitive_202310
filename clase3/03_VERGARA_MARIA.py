import sys

stdin = sys.stdin
case = int(stdin.readline())

total_cases = []
while case != 0:
    total_cases.append(list(range(1,case+1,1)))
    case = int(stdin.readline())

for case in total_cases:
    while len(case)>1:
        case.pop(0)
        case.append(case.pop(0))
    print(case[0])