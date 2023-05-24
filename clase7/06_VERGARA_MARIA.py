from sys import stdin
# import io

# stdin = io.StringIO("""2
# 5
# 4 
# 0 1 
# 1 2
# 3 4
# 7 8 
# 2
# 1 
# 0 1""")

cases = stdin.readlines()

cities = int(cases[0])

def merging(roads):
    final = []
    while len(roads) > 0:
        common = set(roads[0])
        i = 1
        while i < len(roads):
            if common.intersection(roads[i]):
                common.update(roads[i])
                roads.pop(i)
            else:
                i += 1
        final.append(list(common))
        roads.pop(0)
    return final

index = 1
for x in range(cities):
    n = int(cases[index])
    total_roads = int(cases[index+1])
    index += 2
    roads = []
    connections = 0

    for i in range(index, total_roads + index):
        lista = [int(x) for x in cases[i].split()]
        lista.sort()
        roads.append(lista)

    roads = merging(roads)
    
    print(len(roads)-1)
    index += total_roads