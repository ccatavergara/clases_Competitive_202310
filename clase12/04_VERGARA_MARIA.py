# from sys import stdin
import math
import io

stdin = io.StringIO("""6
A 1 0
B 4 0
C 0 3
D 1 3
E 4 4
F 0 6
4
A 0 0
B 1 0
C 99 0
D 99 99
0
""")


def find_biggest_triangle(points):
    max_area = 0
    max_triangle = None

    # Iterate over all possible triangles
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                # Calculate the area of the triangle
                area = 0.5 * abs((y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1))

                # Check if the triangle contains any other points
                contains_other_points = False
                for m in range(len(points)):
                    if m != i and m != j and m != k:
                        x, y = points[m]
                        if (
                            min(x1, x2, x3) <= x <= max(x1, x2, x3) and
                            min(y1, y2, y3) <= y <= max(y1, y2, y3)
                        ):
                            contains_other_points = True
                            break

                # Update the maximum area and triangle if applicable
                if not contains_other_points and area > max_area:
                    max_area = area
                    max_triangle = [(x1, y1), (x2, y2), (x3, y3)]

    return max_triangle


while True:
    line = stdin.readline().split()
    points = {}
    if len(line) == 1:
        cases = int(line[0])
        if cases == 0:
            break
        for x in range(cases):
            point = stdin.readline().split()
            points[point[0]] = [int(x) for x in point[1:]]


    # for x in range(start,cases):
    #     line = lines[start + x - 1].split()
    #     letters[line[0]] = [int(i) for i in line[1: ]]

    # start += cases
    # cases = lines[start]
    # start += 1
    # print(letters)
