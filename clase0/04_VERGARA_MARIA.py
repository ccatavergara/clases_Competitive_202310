from sys import stdin
import io

stdin = io.StringIO("""3
4 5
3 3
4 3""")

for line in stdin.readlines():
    if len(line.split()) > 1: #skips the first line
        data = line.split()
        eats = int(data[0])
        needs = int(data[1])
        
        if eats >= needs:
            print("MMMM BRAINS")
        else:
            print("NO BRAINS")