import sys
input = sys.stdin.readline

a, b = map(int, input().split())

from collections import deque

queue = deque()
queue.append((a, 1))

while queue:
    now, cnt = queue.popleft()

    if now > b:
        continue

    if now == b:
        print(cnt)
        break

    num1 = now*2
    num2 = int(str(now) + '1')
    
    queue.append((num1, cnt+1))
    queue.append((num2, cnt+1))

else:
    print(-1)