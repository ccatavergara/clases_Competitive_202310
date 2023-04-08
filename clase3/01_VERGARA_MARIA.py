import numpy
import math
import sys

stdin = sys.stdin
case = stdin.readline()

cases = []
while case != '0 0\n':
    cases.append(case)
    case = stdin.readline()
    
for case in cases:
    v, v0 = map(int, case.split())

    disc = 0
    max_len = 0
    
    for x in range(1, v + 1):
        vt = v/x
        if vt > v0:
            length = 0.3 * numpy.sqrt(vt-v0) * x
            
            length = (math.trunc(length * 100000)) / 100000
            
            if length > max_len: #el largo del collar va aumentando
                max_len = length
                disc = x
            elif length == max_len:
                disc = 0 #no unique length
                break
            else:
                break
        
        else:
            break
    
    print(disc)
# THE DECIMALS ARE VERY SPECIFIC SO IF THEY ARE NOT THE SAME NUMBER DOWN TO THE 100000TH DECIMAL, IT WON'T COUNT
