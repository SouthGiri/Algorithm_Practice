import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
queue = deque()
ans = []

for _ in range(m):
    small, tall = map(int, input().split())
    graph[small].append(tall)
    inDegree[tall] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*ans)