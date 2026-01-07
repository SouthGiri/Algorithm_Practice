import sys
input = sys.stdin.readline

import heapq

N = int(input())
K = int(input())
data = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

data.sort()

h = []

for i in range(N-1):
    heapq.heappush(h, -(data[i+1] - data[i]))

for _ in range(K-1):
    heapq.heappop(h)

print(abs(sum(h)))