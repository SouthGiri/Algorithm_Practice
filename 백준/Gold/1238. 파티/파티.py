import sys
input = sys.stdin.readline

import heapq
INF = sys.maxsize

def dijkstra(start, end):
    q = []
    node = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    node[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if node[now] < d: continue

        for i in graph[now]:
            dst = i[0]
            cost = d+i[1]

            if cost < node[dst]:
                heapq.heappush(q, (cost, dst))
                node[dst] = cost

    return node[end]

n,m,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

t = 0
for i in range(1, n+1):
    if i == x: continue
    t = max(t, dijkstra(i,x) + dijkstra(x,i))

print(t)