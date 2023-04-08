import numpy
import sys

stdin = sys.stdin
case = stdin.readline()

total_cases = []
while case != '0\n':
    new = [float(x) for x in case.split()]
    total_cases.append(new)
    case = stdin.readline()
    
final_cases = []
for case in total_cases:
    if case[0] == 1:
        u = case[1]
        v = case[2]
        t = case[3]
        a = (v - u)/ t
        s = ((v + u)/2) * t
        final_cases.append(f'{s} {a}')
        
    if case[0] == 2:
        u = case[1]
        v = case[2]
        a = case[3]
        t = (v - u)/ a
        s = ((v + u)/2) * t
        final_cases.append(f'{s} {t}')
    
    if case[0] == 3:
        u = case[1]
        a = case[2]
        s = case[3]
        v = numpy.sqrt(u**2 + 2*a*s)
        t = (v - u)/ a
        final_cases.append(f'{v} {t}')
        
    if case[0] == 4:
        v = case[1]
        a = case[2]
        s = case[3]
        u = numpy.sqrt(u**2 - 2*a*s)
        t = (v - u)/ a
        final_cases.append(f'{u} {t}')
        
for count, case in enumerate(final_cases):
    print(f'Case {count + 1}: ', case)
    
