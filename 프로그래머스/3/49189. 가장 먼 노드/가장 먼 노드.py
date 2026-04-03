import heapq

def dijkstra(n, graph):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[1] = 0
    
    h = []
    heapq.heappush(h, (0, 1))
    
    while h:
        dist, node = heapq.heappop(h)
        if dist > distance[node]:
            continue
        
        for nxt in graph[node]:
            if dist + 1 < distance[nxt]:
                distance[nxt] = dist + 1
                heapq.heappush(h, (dist + 1, nxt))
    
    return distance[1:]
    

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = dijkstra(n, graph)
    answer = distance.count(max(distance))
    
    return answer