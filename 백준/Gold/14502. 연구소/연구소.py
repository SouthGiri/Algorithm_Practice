import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
area = []
empty = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 0:
            empty.append((i, j))
    area.append(line)


def bfs(i, j):
    que = deque()
    que.append((i, j))

    while que:
        row, col = que.popleft()
        dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
        for i in range(4):
            ny, nx = row+dy[i], col+dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                que.append((ny, nx))

wall_list = list(combinations(empty, 3))
ans = 0

for wall in wall_list:
    graph = deepcopy(area)
    # wall graph 에 채우고 bfs 해서 area 구하기
    for w in wall:
        row, col = w
        graph[row][col] = 1

    # bfs
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                bfs(i, j)
    
    safe = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safe += 1
    
    ans = max(ans, safe)

print(ans)