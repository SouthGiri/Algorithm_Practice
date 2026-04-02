from collections import deque

def bfs(row, col, maps):
    dr, dc = (0, 0, -1, 1), (-1, 1, 0, 0)
    N, M = len(maps), len(maps[0])
    
    q = deque()
    q.append((row, col))
    
    while q:
        row, col = q.popleft()
        
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1:
                q.append((nr, nc))
                maps[nr][nc] = maps[row][col] + 1
    
    ans = maps[N-1][M-1]
    return ans if ans != 1 else -1

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer