import sys
input = sys.stdin.readline

import heapq

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
last = data[0][1]
q = []
heapq.heappush(q, last)

for x in data[1:]:
    if x[0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, x[1])

print(len(q))