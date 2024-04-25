import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [list(map(int, (list(input().rstrip())))) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

total = 0
num_house = []

def bfs(start):
    global total
    q = deque()
    q.append(start)
    x, y = start
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1

    total += 1


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            bfs((i,j))
            acc = 0
            for v in visited:
                acc += sum(v)
            num_house.append(acc)

print(len(num_house))


res = [0 for _ in range(len(num_house))]

for i in range(len(num_house)):
    if i == 0:
        res[i] = num_house[i]
    else:
        res[i] = num_house[i] - num_house[i-1]

res.sort()
for i in res:
    print(i)