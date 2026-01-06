import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    # 방문
    graph[y][x] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if graph[ny][nx] == 1:
            dfs(nx, ny)
    

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)