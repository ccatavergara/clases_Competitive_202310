from sys import stdin
# import io

# stdin = io.StringIO("""2
# 1
# 2
# """)

def how_many(length):
    if length == 0 or length == 1:
        print(1)
    elif length == 2:
        print(5)
    else:
        ways = [1,1,5]
        for x in range(3,length+1):
            ways.append(0)
        
        for x in range(3,length+1):
            ways[x] = ways[x-1] + 4 * ways[x - 2] + 2 * ways[x - 3]
        print(ways[-1])
        
cases = int(stdin.readline())

for x in range(cases):
    length = int(stdin.readline())
    how_many(length)
    
    

