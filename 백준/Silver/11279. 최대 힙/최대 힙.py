import sys
input = sys.stdin.readline

import heapq

def push(h, x):
    heapq.heappush(h, -x)

def pop(h):
    try:
        print(-1 * heapq.heappop(h))
    except:
        print(0)


n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x == 0:
        pop(h)
    else:
        push(h, x)