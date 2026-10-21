from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    distS = [INF] * (n+1)
    distA = [INF] * (n+1)
    distB = [INF] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))
        
        
    def dijkstra(start, distances):
        h = []
        heappush(h, (0, start))
        distances[start] = 0
        
        while h:
            cost, now = heappop(h)
            
            if cost > distances[now]:
                continue
            
            for nxt, dist in graph[now]:
                if distances[nxt] > cost + dist:
                    distances[nxt] = cost + dist
                    heappush(h, (cost+dist, nxt))
    
    
    dijkstra(s, distS)
    dijkstra(a, distA)
    dijkstra(b, distB)

    for k in range(1, n+1):
        answer = min(answer, distS[k] + distA[k] + distB[k])

    answer = min(answer, distS[a] + distS[b])
    
    return answer