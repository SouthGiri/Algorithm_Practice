import sys
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9)
distances = [INF] * (N+1)
distances[1] = 0
h = [(0, 1)]

while h:
    cost, node = heapq.heappop(h)

    if cost > distances[node]:
        continue

    for adj_node, adj_cost in graph[node]:
        total_cost = cost + adj_cost
        if total_cost < distances[adj_node]:
            distances[adj_node] = total_cost
            heapq.heappush(h, (total_cost, adj_node))

print(distances[N])