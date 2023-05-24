from sys import stdin
# import io

# stdin = io.StringIO("""5 3
# 1 1 E
# RFRFRFRF
# 3 2 N
# FRRFLLFFRRFLL
# 0 3 W
# LLFFFLFLFL""")

left = ['E', 'N', 'W', 'S', 'E']
right = ['E', 'S', 'W', 'N', 'E']

def direction(d, move):
    if move == "L":
        return left[left.index(d)+1]
    if move == "R":
        return right[right.index(d)+1]

def foward(robot):
    if robot['d'] == 'E':
        robot['x'] += 1
    if robot['d'] == 'W':
        robot['x'] -= 1
    if robot['d'] == 'N':
        robot['y'] += 1
    if robot['d'] == 'S':
        robot['y'] -= 1
    return robot

def conditional(robot):
    return (robot['y'] > width or 
            robot['y'] < 0 or 
            robot['x'] > length or
            robot['x'] < 0)

def fall(robot):
    if robot['y'] > width:
        robot['y'] -= 1
    if robot['y'] < 0:
        robot['y'] += 1
    if robot['x'] > length:
        robot['x'] -= 1
    if robot['x'] < 0:
        robot['x'] += 1
    return robot

def say(robot, lost):
    if lost:
        robot = fall(robot)
        print(robot['x'], robot['y'], robot['d'], 'LOST')
    else:
        print(robot['x'], robot['y'], robot['d'])

def falls_log(robot, falls):
    both = 0
    if robot['x'] not in falls['x']:
        falls['x'].append(robot['x'])
        both += 1
    if robot['y'] not in falls['y']:
        falls['y'].append(robot['y'])
        both += 1
    if both == 2:
        return robot, falls, True
    else:
        robot = fall(robot)
        return robot, falls, False
    
cases = stdin.readlines()

length, width = map(int, cases[0].split())

for i in range(1,len(cases),2): #Sacarle uno a len si hay problema de rango
    x, y, d = map(str, cases[i].split())
    robot = {'x': int(x),
             'y': int(y),
             'd': d}
    movements = cases[i+1]
    lost = False
    falls = {'x': [], 'y':[]}
    for move in movements:
        if move == 'F':
            robot = foward(robot)
            if conditional(robot):
                robot, falls, lost = falls_log(robot, falls)
        elif move == 'R' or move == 'L':
            robot['d'] = direction(robot['d'], move)

    say(robot, lost)