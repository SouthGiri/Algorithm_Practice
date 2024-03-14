import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
    command = list(input().split())
    process = command[0]

    if process == 'push_front':
        dq.insert(0, command[1])
    elif process == 'push_back':
        dq.append(command[1])
    elif process == 'pop_front':
        print(dq.popleft()) if dq else print(-1)
    elif process == 'pop_back':
        print(dq.pop()) if dq else print(-1)
    elif process == 'size':
        print(len(dq))
    elif process == 'empty':
        print(0) if dq else print(1)
    elif process == 'front':
        print(dq[0]) if dq else print(-1)
    else:
        print(dq[-1]) if dq else print(-1)