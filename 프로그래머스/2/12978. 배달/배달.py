from heapq import heappush, heappop

def solution(N, road, K):
    distances = [1e9] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    distances[1] = 0
    h = [(0, 1)]
    
    while h:
        dist, now = heappop(h)
        
        if dist > distances[now]:
            continue
        
        for cost, nxt in graph[now]:
            if dist + cost < distances[nxt]:
                distances[nxt] = dist + cost
                heappush(h, (dist + cost, nxt))
    
    ans = sum(i <= K for i in distances)
    return ans