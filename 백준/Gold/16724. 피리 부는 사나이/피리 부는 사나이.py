import sys
input = sys.stdin.readline

MOVE = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

def dfs(row, col):
    global ans

    path.append((row, col))
    graph[row][col] = 1

    move = moves[row][col]
    dr, dc = MOVE[move]
    nr, nc = row+dr, col+dc
    
    if graph[nr][nc]:
        if graph[nr][nc] == 1:
            ans += 1
        for r, c in path:
            graph[r][c] = 2
        
    else:
        dfs(nr, nc)
    

N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
moves = []
for _ in range(N):
    line = list(input().rstrip())
    moves.append(line)

ans = 0

for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            path = []
            dfs(row, col)

print(ans)