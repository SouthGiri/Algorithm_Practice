import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = [0,0,-1,1], [-1,1,0,0]
res = 0

def dfs(x, y, tmp, cnt):
    global res
    if cnt == 4:
        res = max(res, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n or visited[ny][nx]:
            continue

        visited[ny][nx] = True
        dfs(nx, ny, tmp+paper[ny][nx], cnt+1)
        visited[ny][nx] = False

def fy(x, y):
    global res
    tmp = paper[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n or visited[ny][nx]:
            continue
        arr.append(paper[ny][nx])
    
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        res = max(res, sum(arr) + paper[y][x])
    elif length == 3:
        res = max(res, sum(arr) + paper[y][x])
    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, paper[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(res)