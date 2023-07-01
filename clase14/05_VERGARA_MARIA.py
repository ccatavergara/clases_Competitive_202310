from sys import stdin
# import math
# import io

# stdin = io.StringIO("""2 3
# 5
# 4
# 7
# 8
# 4
# 2 1
# 5
# 5
# 10
# 0 0
# """)

def find_right_knight(head, knights): #this algorithm lets me find the knight that is the same height or the next to tallest one.

    bigger_height = 200000000000000000000
    for height in knights:
        if height >= head and height < bigger_height:
            bigger_height = height #this finds the in between height

    if bigger_height not in knights:
        return -1, knights #if the there is no height it means that no knight is the same size so it returns a -1
    else:
        knights.remove(bigger_height)
    return bigger_height, knights

def find(heads, knights):
    payment = 0

    if len(knights) < len(heads):
        return True #if there are less knights than heads then they are doomed.

    for x in heads:
        result, knights = find_right_knight(x, knights)
        if result == -1: # if there isn-t a knight that matches the height of a head then they are doomed.
            return True
        else:
            payment += result # if there are knights, the payment is added.

    print(payment)

h, k = map(int, stdin.readline().split())

while h != 0 and k != 0:
    heads = []
    knights = []
    for x in range(h):
        heads.append(int(stdin.readline()))
    for y in range(k):
        knights.append(int(stdin.readline()))

    if find(heads, knights):
        print('Loowater is doomed!')

    h, k = map(int, stdin.readline().split())
