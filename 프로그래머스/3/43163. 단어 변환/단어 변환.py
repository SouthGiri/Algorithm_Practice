from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = [begin] + words
    N = len(words)
    visited = [-1] * N
    t = words.index(target)
    
    q = deque([0])
    visited[0] = 0
    
    while q:
        now = q.popleft()
        
        for nxt in range(1, N):
            if visited[nxt] == -1 and sum(a != b for a, b in zip(words[now], words[nxt])) == 1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
                
                if nxt == t:
                    return visited[t]
    
    return 0