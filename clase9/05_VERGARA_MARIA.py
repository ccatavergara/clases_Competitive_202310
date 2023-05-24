# from sys import stdin
import io
import math

stdin = io.StringIO("""5
1
2
3
4
50
""")
terms = [math.inf for x in range(10001)] 

for i in range(1, 101): #100**2 = 10000 so it is the hightest it can go
    for j in range(i * i, 10001):
        terms[j] = min(terms[j], terms[j - i * i] + 1)
        #print(terms[j], terms[j - i * i] + 1, j- i * i)

cases = int(stdin.readline())

for x in range(cases):
    number = int(stdin.readline())
    print(terms[number])