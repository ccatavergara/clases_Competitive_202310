import numpy
import sys

stdin = sys.stdin
case = int(stdin.readline())

for x in range(case):
    an = [int(x) for x in stdin.readline().split()]
    d = int(stdin.readline())
    k = int(stdin.readline())
    bm = []
    
    for i in an:
        for j in range(d*(an.index(i)+1)):
            bm.append(i)

print(bm[k])