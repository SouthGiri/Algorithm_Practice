import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
que = deque()

while True:
    packet = int(input())
    if packet == -1:
        break
    if packet == 0:
        que.popleft()
    else:
        if len(que) < n:
            que.append(packet)

if len(que) == 0:
    print('empty')
while que:
    print(que.popleft(), end=' ')
