from sys import stdin
# import io
import math

# stdin = io.StringIO("""3
# 1
# 2
# 3
# """)

pi = math.acos(-1)

cases = int(stdin.readline())

for case in range(cases):
    l = int(stdin.readline())
    
    circle = round(((l/5)**2) * pi,2)
    rectangle = round(((6/10) * (l**2)) - circle, 2)
    
    print(f'{circle:.2f} {rectangle:.2f}')