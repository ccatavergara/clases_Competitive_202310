import numpy
import sys

stdin = sys.stdin
case = int(stdin.readline())

def exponencial(a, b):
    if b == 0:
        return 1
    if b & 1:
        return a * exponencial((a**2), b//2)
    else:
        return exponencial((a**2), b//2)

for x in range(case):
    c = [int(x) for x in stdin.readline().split()]
    d = int(stdin.readline())
    k = int(stdin.readline())
    n = c.pop(0)
    bm = []
    
    counter_k = 0
    counter_d = 0
    
    i = 1
    while counter_k < k:
        an = 0
        
        for x in range(n + 1):
            an += c[x] * exponencial(i, x)
        counter_d += d
        counter_k += counter_d
        
        i += 1

print(an)