# from sys import stdin
import math
import io

stdin = io.StringIO("""1
5 6
10.00 10.00
20.00 20.00
30.00 10.00
10.00 0.00
9.00 9.00
""")

cases = int(stdin.readline())

def angle(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return angle

def angle(start, end):
        return (math.atan2(end[1]-start[1], end[0] - start[0]))

def calculate_coordinates(point, distance, angle_radians):
    x1, y1 = point
    x2 = x1 + distance * math.cos(angle_radians)
    y2 = y1 + distance * math.sin(angle_radians)
    return x2, y2

for case in range(cases):
    k,t = map(int, stdin.readline().split())
    points = []
    for y in range(k):
        points.append([float(i) for i in stdin.readline().split()])

    total_distance = 0
    for x in range(1,len(points)):
        total_distance += math.dist(points[x-1],points[x])


    distance_between = total_distance/t

    angle = angle(points[0],points[1])
    coordinates = calculate_coordinates(points[0], distance_between, angle)
    print(coordinates)
