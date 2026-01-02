import sys
input = sys.stdin.readline

import heapq

bags = []
jewels = []

N, K = map(int, input().split())
for _ in range(N):
    weight, value = map(int, input().split())
    jewels.append((weight, value))
for _ in range(K):
    bags.append(int(input()))

bags.sort()
jewels.sort()

h = []
ans = 0
idx = 0

for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(h, -jewels[idx][1])
        idx += 1
    if h:
        ans += -heapq.heappop(h)

print(ans)