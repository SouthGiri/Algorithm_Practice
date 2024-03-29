import sys
input = sys.stdin.readline

# 익은 토마토 상하좌우 -> 익음
# 모든 토마토가 익는 최소 일수

from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1,1,0,0], [0,0,-1,1]
day = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

bfs()
for line in tomato:
    for i in line:
        if i == 0:
            print(-1)
            exit()
    day = max(day, max(line))
print(day-1)
