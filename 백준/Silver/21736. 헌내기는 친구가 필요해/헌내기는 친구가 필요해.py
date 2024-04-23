import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

dx, dy = [0,0,-1,1], [-1,1,0,0]
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
where = ['I' in graph[i] for i in range(n)]
row = where.index(True)
start = (row, graph[row].index('I'))
q = deque()
q.append(start)

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'X' and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = 1
            if graph[nx][ny] == 'P':
                cnt += 1

print(cnt) if cnt > 0 else print('TT')
            