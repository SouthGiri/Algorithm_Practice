def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    
    board = [[0] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, r)

        for x, y in ((_x, _y) for _x in range(x1+1, x2) for _y in range(y1+1, y2)):
            board[y][x] = 2
        
        for x, y in ((_x, _y) for _x in range(x1, x2+1) for _y in (y1, y2)):
            if board[y][x] == 0:
                board[y][x] = 1
            
        for x, y in ((_x, _y) for _x in (x1, x2) for _y in range(y1, y2+1)):
            if board[y][x] == 0:
                board[y][x] = 1
                
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((characterX*2, characterY*2))
    visited = [[0] * 102 for _ in range(102)]
    visited[characterY*2][characterX*2] = 1
    
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visited[y][x] // 2
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))
    
    return answer
