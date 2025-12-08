import sys
input = sys.stdin.readline

from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    visited = [[0] * N for _ in range(N)]
    q = deque([[r, c]])
    visited[r][c] = 1
    cand = []

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if graph[nr][nc] <= shark_size:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

                    if graph[nr][nc] < shark_size and graph[nr][nc] != 0:
                        cand.append((visited[nr][nc], nr, nc))
    
    return sorted(cand)

N = int(input())
graph = []
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c] == 9:
            shark_row, shark_col = r, c
    graph.append(line)

shark_size = 2
eat = 0
ans = 0

while True:
    shark = bfs(shark_row, shark_col)
    
    if len(shark) == 0:
        break

    dist, nr, nc = shark[0]

    graph[shark_row][shark_col], graph[nr][nc] = 0, 0
    shark_row, shark_col = nr, nc
    
    eat += 1
    if eat == shark_size:
        shark_size += 1
        eat = 0

    ans += dist-1

print(ans)