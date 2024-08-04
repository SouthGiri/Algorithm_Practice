import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra(start, end):
    distance = [inf] * (n+1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heappop(heap)
        if cost > distance[now]: continue

        for node, weight in graph[now]:
            acc_cost = cost + weight
            if distance[node] > acc_cost:
                distance[node] = acc_cost
                heappush(heap, (acc_cost, node))

    return distance[end]


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

inf = sys.maxsize

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= inf and path2 >= inf:
    print(-1)
else:
    print(min(path1, path2))