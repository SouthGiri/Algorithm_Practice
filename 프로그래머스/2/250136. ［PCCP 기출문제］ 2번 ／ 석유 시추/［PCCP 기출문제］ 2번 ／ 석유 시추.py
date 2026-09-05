def solution(land):
    N, M = len(land), len(land[0])
    cols = [0] * M
    visited = [[False] * M for _ in range(N)]
    
    def bfs(r, c):        
        from collections import deque
        
        q = deque()
        q.append((r, c))
        visited[r][c] = True
        dr, dc = (0, 0, -1, 1), (-1, 1, 0, 0)
        oil = 1
        _cols = set()
        _cols.add(c)
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and land[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    oil += 1
                    _cols.add(nc)
        
        for c in _cols:
            cols[c] += oil
    
    
    for r, c in ((_r, _c) for _r in range(N) for _c in range(M)):
        if land[r][c] == 1 and not visited[r][c]:
            bfs(r, c)
    
    answer = max(cols)
    return answer