import sys
input = sys.stdin.readline

from collections import deque

avail = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (2, -1), (2, 1), (1, -2), (1, 2))

def bfs(row, col):
    q = deque()
    q.append((row, col))

    while q:
        r, c = q.popleft()
        for dr, dc in avail:
            nr, nc = r+dr, c+dc
            
            if 0 <= nr < L and 0 <= nc < L and board[nr][nc] == 0:
                q.append((nr, nc))
                board[nr][nc] = board[r][c] + 1

                if [nr, nc] == dst:
                    print(board[nr][nc])
                    return


T = int(input())
for _ in range(T):
    L = int(input())
    board = [[0] * L for _ in range(L)]
    
    src = list(map(int, input().split()))
    dst = list(map(int, input().split()))

    if src == dst:
        print(0)
    else:
        bfs(*src)