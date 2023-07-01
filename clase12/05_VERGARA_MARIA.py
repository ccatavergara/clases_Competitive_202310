from sys import stdin
import math
# import io

# stdin = io.StringIO("""12.0 12.0 8.0
# """)

lines = stdin.readlines()

def radius(a,b,c):
    x = 4*(a*a)*(b*b) - ((a*a) + (b*b) - (c*c))**2
    y = 2*(a + b + c)
    x = math.sqrt(x)
    return x/y

for line in lines:
    a,b,c = map(float, line.split())
    if a == 0 or b == 0 or c == 0:
        print(f'The radius of the round table is: 0.000')
    else:
        print(f'The radius of the round table is: {round(radius(a,b,c),3):.3f}')
