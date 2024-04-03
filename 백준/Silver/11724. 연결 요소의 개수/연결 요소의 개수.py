import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        for node in mat[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    global connection
    connection += 1

n, m = map(int, input().split())

visited = [0] * (n+1)
mat = [[] for _ in range(n+1)]
connection = 0

for _ in range(m):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)

print(connection)