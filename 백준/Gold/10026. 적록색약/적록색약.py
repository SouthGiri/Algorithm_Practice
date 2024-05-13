import sys
input = sys.stdin.readline

from collections import deque
import copy

dr, dc = [0,0,-1,1], [-1,1,0,0]

def bfs(i, j, graph):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    color = graph[i][j]
    while queue:
        row, col = queue.popleft()
        #color = graph[row][col]
        
        for i in range(4):
            nr, nc = row + dr[i], col+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                clr = graph[nr][nc]

                if not visited[nr][nc] and color == clr:
                    queue.append([nr, nc])
                    visited[nr][nc] = True

n = int(input())

visited = [[0]*n for _ in range(n)]
graph = [list(input().rstrip()) for _ in range(n)]
ab_graph = copy.deepcopy(graph)

normal = 0
abnormal = 0

for i in range(n):
    for j in range(n):
        if ab_graph[i][j] == 'R':
            ab_graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph=graph)
            normal += 1

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph=ab_graph)
            abnormal += 1

print(normal, abnormal)