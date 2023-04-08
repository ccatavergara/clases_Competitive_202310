
from sys import stdin
import io

stdin = io.StringIO("""10 2 1
20 3 1
0 0 0""")

for line in stdin.readlines():
    if line != "0 0 0":
        data = line.split()
        n = int(data[0])
        u = int(data[1])
        d = int(data[2])

        minutes = 0
        while n > 0:
            minutes += 1
            n -= u
            if n > 0:
                minutes += 1
                n += d
            
        print(minutes)

            