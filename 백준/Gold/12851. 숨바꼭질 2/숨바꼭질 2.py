import sys
input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque

que = deque()
que.append(n)
time = [-1]*100_001
time[n] = 0
cnt = 0

while que:
    loc = que.popleft()
    if loc == k:
        cnt += 1

    for nxt_loc in (loc-1, loc+1, loc*2):
        if 0 <= nxt_loc <= 100000:
            if time[nxt_loc] == -1 or time[nxt_loc] >= time[loc] + 1:
                time[nxt_loc] = time[loc] + 1
                que.append(nxt_loc)

print(time[k])
print(cnt)