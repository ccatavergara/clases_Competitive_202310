from sys import stdin
import io

stdin = io.StringIO("""1 3
3 2 1
3
3 5 3 2
3 5 3 1
3 1 1 1
3 10
1 2 3 4 5 6 7 8 9 10
10 1 2 3 4 5 6 7 8 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
2 4
1 3 4 2
4 1 3 2
2
3 3 2 1
3 5 4 2
0 0""")

for line in stdin.readlines():
    while line != "0 0":
        races = 