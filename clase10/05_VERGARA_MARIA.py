from sys import stdin
# import io

# stdin = io.StringIO("""1
# 3 6 7
# 1 7 5 4 8 3 9
# 1 4 3 5 6 2 8 9
# """)

cases = int(stdin.readline())

# guru99.com/longest-common-subsequence.html#:~:text=What%20is%20Longest%20Common%20Subsequence,in%20both%20strings%20or%20patterns.
#this is the longest common subsequence that we saw in class. This is because you need to find the common items, or numbers in this case that go in order. It does not count if you have similar numbers if they are not in a sequence - not necessarly one after the other.

def similar_route(prince, princess):
    prince_ = len(prince)
    princess_ = len(princess)
    # matrix will store the solutions as the 
    matrix = [
        [0] * (princess_ + 1) for x in range(prince_ + 1)
    ]
    for i in range(prince_ + 1):
        for j in range(princess_ + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif prince[i - 1] == princess[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else :
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[prince_][princess_]

    
for x in range(cases):
    n, p, q = map(int, stdin.readline().split())
    prince = [int(x) for x in stdin.readline().split()]
    princess = [int(x) for x in stdin.readline().split()]

    route = similar_route(prince,princess)
    print(f'Case {x+1}: {route}')