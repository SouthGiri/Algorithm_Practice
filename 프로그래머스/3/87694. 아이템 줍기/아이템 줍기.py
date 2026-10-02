from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 101
    rectangle = [(2 * a, 2 * b, 2 * c, 2 * d) for a, b, c, d in rectangle]
    cx, cy = 2*characterX, 2*characterY
    ix, iy = 2*itemX, 2*itemY
    
    graph = [[0] * (N) for _ in range(N)]
    
    def is_in(x, y):
        return any(e < x < g and f < y < h for e,f,g,h in rectangle)

    
    for a,b,c,d in rectangle:
        for x in range(a, c+1):
            for y in (b, d):
                if not is_in(x, y):
                    graph[x][y] = 1
        
        for y in range(b, d+1):
            for x in (a, c):
                if not is_in(x, y):
                    graph[x][y] = 1
        
    visited = [[-1] * N for _ in range(N)]
    visited[cx][cy] = 0
    q = deque([(cx, cy)])
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == (ix, iy):
            return visited[ix][iy] // 2
        
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return 0