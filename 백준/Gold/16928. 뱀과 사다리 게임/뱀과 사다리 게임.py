import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

ladder = {}
snake = {}
visited = [0] * 101
board = [0] * 101

for _ in range(n):
    src, dst = map(int, input().split())
    ladder[src] = dst

for _ in range(m):
    src, dst = map(int, input().split())
    snake[src] = dst


# bfs
q = deque()
q.append(1)
while q:
    x = q.popleft()
    if x == 100:
        break

    for dice in range(1, 7):
        nxt_loc = x + dice

        if nxt_loc <= 100 and not visited[nxt_loc]:
            if nxt_loc in ladder:
                nxt_loc = ladder[nxt_loc]
                
            if nxt_loc in snake:
                nxt_loc = snake[nxt_loc]
            
            if not visited[nxt_loc]:
                visited[nxt_loc] = True
                board[nxt_loc] = board[x] + 1
                q.append(nxt_loc)


print(board[100])