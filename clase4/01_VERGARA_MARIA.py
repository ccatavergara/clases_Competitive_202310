# from sys import stdin
# import io

# stdin = io.StringIO("""6
# 5 19
# 55 28
# 38 101
# 28 62
# 111 84
# 43 116
# 5
# 11 27
# 84 99
# 142 81
# 88 30
# 95 38
# 3
# 132 73
# 49 86
# 72 111
# 0""")

#Getting in Line

import sys 
stdin = sys.stdin

def distance(a, b):
    return round((((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5) + 16,2)

def selection(points):
    min_dist = 100000
    first = points[0]
    index = 1
    for x in range(1,len(points)):
        dist = distance(first, points[x])
        if dist < min_dist:
            min_dist = dist
            index = x
    return min_dist, index

def passing(points, number):
    print("*******************************************************")
    print(f'Network #{number}')
    total_dist = 0
    while len(points) > 1:
        min_dist, index = selection(points)
        print(f'Cable requiremente to connect {points[0]} to {points[index]} is {min_dist} feet.')
        total_dist += min_dist
        points[0] = points[index]
        points.pop(index)
    print(f'Number of feet of cable required is {total_dist}.')
    return number + 1

lines = int(stdin.readline())
number = 1
while lines != 0:
    points = []
    for line in range(lines):
        points.append([int(x) for x in stdin.readline().split()])
    
    number = passing(points, number)
    lines = int(stdin.readline())

        


