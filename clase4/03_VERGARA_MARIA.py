map = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

ans = [0] * 8

def DFS(idx, now):
    ans[idx] = now
    if idx == 8:
        for i in range(9):
            print(ans[i]+1, end="")
        print()
        return
    
    for i in range(5):
        if map[now][i] == 1:
            map[now][i] = map[i][now] = 0
            DFS(idx+1, i)
            map[now][i] = map[i][now] = 1

def main():
    DFS(0, 0)
    return 0

if __name__ == '__main__':
    main()
