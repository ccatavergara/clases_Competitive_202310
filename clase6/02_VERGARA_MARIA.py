from sys import stdin
# import io

# stdin = io.StringIO("""3
# 1 2 0
# 2 2 0
# 3 1 2 0
# 0
# 2 1 2
# 0""")

lines = (stdin.readlines())

vertex = int(lines[0])
roads = {}
for x in range(1, vertex + 1):
    line = [int(x) for x in lines[x].split()]
    roads[line[0]] = line[1:-1]

vertex += 2
while lines[vertex] != '0':
    linea = [int(x) for x in lines[vertex].split()]
    total = linea.pop(0)
    for key in linea:
        keys = list(roads.keys())
        for item in roads[key]:
            keys.remove(item)
        final = f'{len(keys)}'
        for k in keys:
            final += f' {k}'
        print(final)
    vertex += 1
