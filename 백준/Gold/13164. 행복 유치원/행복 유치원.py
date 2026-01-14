import sys
input = sys.stdin.readline

import heapq

N, K = map(int, input().split())
data = list(map(int, input().split()))

diff = [data[i] - data[i+1] for i in range(N-1)]
heapq.heapify(diff)

for _ in range(K-1):
    heapq.heappop(diff)

print(-sum(diff))