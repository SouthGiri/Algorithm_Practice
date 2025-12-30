import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_deg = [0] * (N+1)
in_deg[0] = -1

for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(1, data[0]):
        src, dst = data[i], data[i+1]
        if dst not in graph[src]:
            graph[src].append(dst)
            in_deg[dst] += 1

q = deque()
for i in range(N+1):
    if in_deg[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for dst in graph[now]:
        in_deg[dst] -= 1
        if in_deg[dst] == 0:
            q.append(dst)

if len(ans) != N:
    print(0)
else:
    for x in ans:
        print(x)