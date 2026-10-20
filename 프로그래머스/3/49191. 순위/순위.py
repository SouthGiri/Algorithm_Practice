from collections import deque

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    rev_graph = [[] for _ in range(n+1)]
    
    sc1 = [0] * (n+1)
    sc2 = [0] * (n+1)
    
    for win, lose in results:
        graph[win].append(lose)
        rev_graph[lose].append(win)
    
    
    def bfs(start, g, score):
        visited = [False] * (n+1)
        
        q = deque([start])
        visited[start] = True
        
        while q:
            node = q.popleft()
            
            for nxt in g[node]:
                if not visited[nxt]:
                    q.append(nxt)
                    visited[nxt] = True
                    score[start] += 1
        
    for node in range(1, n+1):
        bfs(node, graph, sc1)
        bfs(node, rev_graph, sc2)
        
        if sc1[node] + sc2[node] == n-1:
            answer += 1
    
    return answer