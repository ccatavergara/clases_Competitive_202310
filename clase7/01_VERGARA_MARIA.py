import heapq

# from sys import stdin
import io

stdin = io.StringIO("""2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5""")

cases = stdin.readlines()

# define the possible moves as offsets from the current position
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# define a function to run Dijkstra's algorithm
def dijkstra(maze):
    n = len(maze)
    m = len(maze[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = maze[0][0]
    heap = [(maze[0][0], 0, 0)]
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == n - 1 and y == m - 1:
            return dist[n - 1][m - 1]
        if cost > dist[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = cost + maze[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

# read in the input

num_mazes = int(cases[0])
index = 1
for x in range(num_mazes):
    n = int(cases[index])
    m = int(cases[index+1])
    maze = []
    for _ in range(n):
        row = list(map(int, input().split()))
        maze.append(row)
    # run Dijkstra's algorithm and print the result
    result = dijkstra(maze)
    print(result)
    index += (n+1)