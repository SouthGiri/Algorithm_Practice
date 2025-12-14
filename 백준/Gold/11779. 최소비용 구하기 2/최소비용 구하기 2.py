import sys
input = sys.stdin.readline

import heapq

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))

    while h:
        cost, now = heapq.heappop(h)

        if distance[now] < cost:
            continue

        for adj, dist in graph[now]:
            if cost + dist < distance[adj]:
                distance[adj] = cost + dist
                prev[adj] = now
                heapq.heappush(h, (cost+dist, adj))

def print_travel():
    print(distance[end])
    
    ans = [end]
    while ans[-1] != start:
        ans.append(prev[ans[-1]])
    
    print(len(ans))
    print(*ans[::-1])
        
        

INF = 1e9
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst, cost = map(int, input().split())
    graph[src].append((dst, cost))

start, end = map(int, input().split())

distance = [INF] * (N+1)
prev = [start] * (N+1)

dijkstra(start)
print_travel()