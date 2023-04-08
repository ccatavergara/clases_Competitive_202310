
from sys import stdin
import io

stdin = io.StringIO("""11 54
a
b
c
d
e
f
g
h
i
j
k
a 1 - 0 b
a 1 - 0 c
a 1 - 0 d
a 1 - 0 e
a 1 - 0 f
a 1 - 0 g
a 1 - 0 h
a 1 - 0 i
a 1 - 0 j
a 1 - 0 k
b 1 - 0 c
b 1 - 0 d
b 1 - 0 e
b 1 - 0 f
b 1 - 0 g
b 1 - 0 h
b 1 - 0 i
b 1 - 0 j
b 1 - 0 k
c 1 - 0 d
c 1 - 0 e
c 1 - 0 f
c 1 - 0 g
c 1 - 0 h
c 1 - 0 i
c 1 - 0 j
c 1 - 0 k
d 1 - 0 e
d 1 - 0 f
d 1 - 0 g
d 1 - 0 h
d 1 - 0 i
d 1 - 0 j
d 1 - 0 k
e 1 - 0 f
e 1 - 0 g
e 1 - 0 h
e 1 - 0 i
e 1 - 0 j
e 1 - 0 k
f 1 - 0 g
f 1 - 0 h
f 1 - 0 i
f 1 - 0 j
f 1 - 0 k
g 1 - 0 h
g 1 - 0 i
g 1 - 0 j
g 1 - 0 k
h 1 - 0 i
h 1 - 0 j
h 1 - 0 k
i 1 - 0 j
i 1 - 0 k
0 0""")

total_teams, total_games = [int(x) for x in stdin.readline().split()]

teams = {}

for x in range(total_teams):
    teams[stdin.readline().replace('\n','')] = {'played': 0, 'win_scored': 0, 'suffered': 0, 'draw_scored': 0, 'win': 0}

for x in range(total_games):
    statistics = stdin.readline().split()
    
    teams[statistics[0]]['played'] += 1
    teams[statistics[4]]['played'] += 1
    
    if int(statistics[3]) == int(statistics[1]):
        teams[statistics[0]]['played'] += 1
        teams[statistics[4]]['played'] += 1
        
        teams[statistics[0]]['draw_scored'] += int(statistics[3])
        teams[statistics[4]]['draw_scored'] += int(statistics[1])
        
    else:  
        teams[statistics[0]]['win_scored'] += int(statistics[1])
        teams[statistics[4]]['win_scored'] += int(statistics[3])
        
        teams[statistics[0]]['suffered'] += int(statistics[3])
        teams[statistics[4]]['suffered'] += int(statistics[1])
    

for count, team in enumerate(teams):
    print(count+1, team, teams[team]['played'] + teams[team]['scored'] + (teams[team]['scored'] - teams[team]['suffered']),teams[team]['played'], teams[team]['scored'], teams[team]['suffered'], teams[team]['scored'] - teams[team]['suffered'], (teams[team]['scored']/ teams[team]['played'])*100)
    
    