from sys import stdin
# import math
# import io

# stdin = io.StringIO("""1 2 3 4 5
# 5 4 3 2 1
# 5 1 2 3 4
# 7 1 6 5 3 4 8 2
# """)

cases = stdin.readlines()

def flip(line, num):
    if num == 0: # this allows to select the section of the line that needs to be switched.
        sort = line
    else:
        sort = line[num:]

    sort.reverse()
    line[num:] = sort
    return line

def f(final, line):
    final.sort() #the correcto order
    switch = []
    turn = 1 # this lets us know if it starts with the biggest number of the line or not.
    while line != final:
        biggest = max(line)
        index = line.index(biggest)
        if index == final.index(biggest): # if the biggest number of the line is in the correct position, we have to shorten the list.
            final.pop(index)
            line.pop(index)
        else:
            line = flip(line, index)
            switch.append(index + turn)
            turn += 1
    switch.append(0)
    return switch

for case in cases:
    line = [int(x) for x in case.split()] # the line that is going to change
    final = [int(x) for x in case.split()]
    original = [(x) for x in case.split()]

    switch = f(final, line)


    str_switch = [str(x) for x in switch]
    print(' '.join(original))
    if len(switch) == 1:
        print(0)
    else:
        print(' '.join(str_switch))


