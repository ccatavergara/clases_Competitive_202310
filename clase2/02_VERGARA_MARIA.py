import sys

stdin = sys.stdin
cases = int(stdin.readline())

for x in range(cases):
    final = abs(int(stdin.readline()))
    
    minimum = 0
    while x in range(final*2):
        