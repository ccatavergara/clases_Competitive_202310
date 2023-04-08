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
    board, bishops = map(int, case.split())