import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
start, end = map(int, input().split())
m = int(input())
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

ans = -1
visit = [0] * 100
def dfs(x, cnt):
    visit[x] = True
    
    if x == end:
        global ans
        ans = cnt
    
    for nxt in graph[x]:
        if not visit[nxt]:
            dfs(nxt, cnt+1)

dfs(start, 0)
print(ans)