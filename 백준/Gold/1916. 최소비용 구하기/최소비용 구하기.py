import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = sys.maxsize
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dp = [inf for _ in range(n+1)]

for _ in range(m):
    src, dst, wei = map(int, input().split())
    graph[src].append((dst, wei))

start, goal = map(int, input().split())

def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        cost, dest = heappop(heap)
        if dp[dest] < cost:
            continue
        for node, wei in graph[dest]:
            accu_cost = cost + wei
            if dp[node] > accu_cost:
                dp[node] = accu_cost
                heappush(heap, (accu_cost, node))

dijkstra(start)
print(dp[goal])