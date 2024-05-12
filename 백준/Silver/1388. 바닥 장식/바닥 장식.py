import sys
input = sys.stdin.readline
# 1388
n, m = map(int, input().split())

floor = [list(input().rstrip()) for _ in range(n)]

def dfs(y, x):
    if floor[y][x] == '-':
        floor[y][x] = 1
        for dx in [1, -1]:
            nx = x + dx
            if 0 <= nx < m and floor[y][nx] == '-':
                dfs(y, nx)
    
    if floor[y][x] == '|':
        floor[y][x] = 1
        for dy in [1, -1]:
            ny = y + dy
            if 0 <= ny < n and floor[ny][x] == '|':
                dfs(ny, x)
        
cnt = 0

for i in range(n):
    for j in range(m):
        if floor[i][j] == '|' or floor[i][j] == '-':
            dfs(i, j)
            cnt += 1

print(cnt)