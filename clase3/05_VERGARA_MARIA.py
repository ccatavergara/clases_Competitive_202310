from sys import stdin
import io

stdin = io.StringIO("""5
                    14
                    42""")

catalan = [1 for i in range(26)]
for i in range(1,26):
    catalan[i] = ((4*i + 2) * catalan[i-1]) / (i + 2)
    
for line in stdin.readlines():
    if int(line) in catalan:
        print(catalan.index(int(line))+1)