from sys import stdin
# import io
# import math

# stdin = io.StringIO("""
# """)

def intersect(b1, b2, c1, c2):
    x1 = max(a1, c1)
    y1 = max(a2, c2)
    x2 = min(b1, d1)
    y2 = min(b2, d2)

    width = x2 - x1
    height = y2 - y1

    if width < 0 or height < 0:
        return 0
    else:
        return width * height

def area_med(a1,a2,b1,b2,c1,c2,d1,d2):
    x1 = abs(b1 - a1)
    x2 = abs(d1 - c1)
    y1 = abs(b2 - a2)
    y2 = abs(d2 - c2)
    
    return (x1*y1) + (x2*y2)

cases = int(stdin.readline())

for case in range(cases):
    a1,a2,b1,b2 = map(int, stdin.readline().split())
    c1,c2,d1,d2 = map(int, stdin.readline().split())

    if intersect(b1,b2,c1,c2) > 0:
        area_s = intersect(b1,b2,c1,c2)
        area_m = area_med(a1,a2,b1,b2,c1,c2,d1,d2) - (2*area_s)
        area_l = (100*100) - abs(area_m) - abs(area_s)
    else:
        area_s = 0
        area_m = area_med(a1,a2,b1,b2,c1,c2,d1,d2)
        area_l = (100*100) - abs(area_m)

    print(f'Night {case+1}: {area_s} {abs(area_m)} {area_l}')