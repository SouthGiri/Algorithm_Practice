import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    command = list(input().split())
    proc = command[0]

    if proc == 'push':
        queue.append(int(command[1]))
    elif proc == 'pop':
        print(queue.popleft()) if len(queue) != 0 else print(-1)
    elif proc == 'size':
        print(len(queue))
    elif proc == 'empty':
        print(1) if len(queue) == 0 else print(0)
    elif proc == 'front':
        print(queue[0]) if len(queue) != 0 else print(-1)
    else:
        print(queue[-1]) if len(queue) != 0 else print(-1)