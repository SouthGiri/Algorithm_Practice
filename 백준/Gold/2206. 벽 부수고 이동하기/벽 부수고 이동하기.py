import sys
input = sys.stdin.readline

from collections import deque


def bfs(x,y,z):
    que = deque()
    que.append((x,y,z))
    
    while que:
        x,y,z = que.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][z]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= nx < n and 0 <= ny < m:
                # wall and not broken
                if graph[nx][ny] == 1 and z == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    que.append((nx, ny, 1))
                # can move and not visit
                elif graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    que.append((nx, ny, z))
    
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

print(bfs(0,0,0))