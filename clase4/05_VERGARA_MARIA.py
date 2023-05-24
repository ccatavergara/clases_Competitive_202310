# Settlers of Catan

import sys 
stdin = sys.stdin

nodes, edges = map(int, stdin.readline().split())

while nodes != 0 and edges != 0:
    points = []
    for x in range(edges):
        points.append([int(x) for x in stdin.readline().split()])

    tracker = point[0][0]
    
    
    
    for point in points:
        print(points)
    nodes, edges = map(int, stdin.readline().split())
    