from collections import deque

def solution(n, edge):
    dist = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    dist[1] = 0
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if dist[nxt] == -1:
                q.append(nxt)
                dist[nxt] = dist[now] + 1
    
    answer = dist.count(max(dist))
        
    return answer