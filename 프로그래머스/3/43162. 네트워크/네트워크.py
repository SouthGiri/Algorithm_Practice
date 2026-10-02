def solution(n, computers):
    from collections import deque
    
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            print(i)
            
            while q:
                node = q.popleft()
                
                for j, connected in enumerate(computers[node]):
                    if not visited[j] and connected:
                        q.append(j)
                        visited[j] = True
            
            answer += 1
            
    return answer