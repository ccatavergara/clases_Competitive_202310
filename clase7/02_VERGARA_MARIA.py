# from sys import stdin
import io

stdin = io.StringIO("""7
11 12 2500
14 17 1500
9 9 750
7 15 600
19 16 500
8 18 400
15 21 250
0""")

cases = stdin.readlines()

total = int(cases[0])
islands = []

for x in range(1,total + 1):
    islands.append([int(x) for x in cases[x].split()])
    
import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {start: 0}
    while queue:
        (dist, node) = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, distance in graph[node].items():
            new_distance = dist + distance
            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    return distances

group = 1
while True:
    n = total
    if n == 0:
        break
    graph = {}
    for i in range(1, total + 1):
        x, y, m = map(int, cases[i].split())
        node = (x, y)
        graph[node] = {}
        for j in range(i):
            other_node = list(graph.keys())[j]
            distance = ((node[0] - other_node[0])**2 + (node[1] - other_node[1])**2)**0.5
            graph[node][other_node] = distance
            graph[other_node][node] = distance
    distances = dijkstra(graph, list(graph.keys())[0])
    connection_times = [distances[node] / 1.0 for node in graph]
    weighted_sum = sum(m * t for (m, t) in zip([node[2] for node in graph], connection_times))
    total_inhabitants = sum(node[2] for node in graph)
    average_time = weighted_sum / total_inhabitants
    print("Island Group: %d Average %.2f" % (group, average_time))
    print()
    group += 1
