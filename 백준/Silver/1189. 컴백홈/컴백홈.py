import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(r)]

dx, dy = [0,0,-1,1], [-1,1,0,0]
res = 0

def dfs(x, y, dist):
    global res
    if x == 0 and y == c-1 and dist == k:
        res += 1

    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = 'T'
                dfs(nx, ny, dist+1)
                graph[nx][ny] = '.'

graph[r-1][0] = 'T'
dfs(r-1, 0, 1)

print(res)