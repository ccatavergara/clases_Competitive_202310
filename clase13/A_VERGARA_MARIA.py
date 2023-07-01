from sys import stdin
# import math
# import io

# stdin = io.StringIO("""2 2
# 3 0
# """)

player_1 = [int(x) for x in stdin.readline().split()]
player_2 = [int(x) for x in stdin.readline().split()]

points_1 = player_1[0]*3 + player_1[1]
points_2 = player_2[0]*3 + player_2[1]

dif = points_1 - points_2

if dif > 0:
    print(1, dif)
elif dif < 0:
    print(2, -dif)
else:
    print('NO SCORE')
