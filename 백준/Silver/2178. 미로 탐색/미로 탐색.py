import sys
input = sys.stdin.readline

from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx, dy = [0,0,-1,1], [-1,1,0,0]

q = deque()
q.append((0, 0))


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
            mat[nx][ny] = mat[x][y] + 1
            q.append((nx, ny))

print(mat[n-1][m-1])