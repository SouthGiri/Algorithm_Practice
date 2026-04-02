from collections import deque

visited = []

def bfs(start, computers):
    global visited
    
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        for nxt, is_connected in enumerate(computers[now]):
            if is_connected and not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
    

def solution(n, computers):
    answer = 0
    global visited
    visited = [False] * n
    
    for computer in range(n):
        if not visited[computer]:
            bfs(computer, computers)
            answer += 1
    
    return answer