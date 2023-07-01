# from sys import stdin
import math
import io

stdin = io.StringIO("""2 1
""")

lines = stdin.readlines()

for line in lines:
    m,n = map(int, line.split())

    total_walls = 0
    for x in range(n):
        if x % 2 != 0:
            total_walls += (4 + 3 * (m - 2)) #all the even lines have the same formula related to m
        elif x == 0:
            total_walls += (6 + 5 * (m-1)) # the first row is the most important because it is complete
        else:
            total_walls += (10 + 3 * (m - 2)) # the odd walls are constructed around the even lines

    print(total_walls)
