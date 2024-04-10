import sys
input = sys.stdin.readline

import heapq
from math import inf

vert, edge = map(int, input().split())
first_node = int(input())

dist_list = [inf] * (vert+1)
graph = [[] for _ in range(vert+1)]

for _ in range(edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist_list[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist_list[node] < dist:
            continue
        for next in graph[node]:
            cost = dist_list[node] + next[1]
            if cost < dist_list[next[0]]:
                dist_list[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(first_node)

for i in range(1, vert+1):
    if dist_list[i] == inf:
        print('INF')
    else:
        print(dist_list[i])