import sys
input = sys.stdin.readline

graph = []
r, c = map(int, input().split())
for _ in range(r):
    graph.append(list(input().rstrip()))

ans = 0
alphabet = set()
dx, dy = [0,0,-1,1], [-1,1,0,0]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in alphabet:
            alphabet.add(graph[nx][ny])
            dfs(nx, ny, cnt+1)
            alphabet.remove(graph[nx][ny])

alphabet.add(graph[0][0])
dfs(0, 0, 1)
print(ans)