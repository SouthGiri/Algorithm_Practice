def dfs():
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.remove(i)


N, M = map(int, input().split())
arr = []
dfs()