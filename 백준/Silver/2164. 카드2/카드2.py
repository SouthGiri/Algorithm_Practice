import sys
input = sys.stdin.readline
from collections import deque

# 1. 맨 위 카드 버리기 2. 맨 위 카드 맨 아래로 넣기
# 마지막 남은 카드

n = int(input())
q = deque(i for i in range(1, n+1))
cnt = 0

while len(q) != 1:
    if cnt % 2 == 0:
        q.popleft()
    else:
        q.append(q.popleft())
    cnt += 1
print(q.pop())