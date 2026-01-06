import sys
input = sys.stdin.readline

from collections import deque

dr, dc = (0, 0, -1, 1), (-1, 1, 0, 0)

def transfer(r, c, idx):
    q = deque()
    q.append((r, c))
    country = [(r, c)]
    united[r][c] = idx
    population = graph[r][c]

    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and \
                united[nr][nc] == -1 and L <= abs(graph[r][c] - graph[nr][nc]) <= R: 
                
                q.append((nr, nc))
                country.append((nr, nc))
                united[nr][nc] = idx
                population += graph[nr][nc]
        
    for r, c in country:
        graph[r][c] = int(population / len(country))


N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

ans = 0

while True:
    united = [[-1] * N for _ in range(N)]
    idx = 0

    for r in range(N):
        for c in range(N):
            if united[r][c] == -1:
                transfer(r, c, idx)
                idx += 1

    if idx == N*N:
        break

    ans += 1

print(ans)