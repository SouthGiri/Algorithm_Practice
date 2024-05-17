import sys
input = sys.stdin.readline

import heapq

n = int(input())
heap = []

# heap 부호와 절댓값을 튜플로 저장
for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x//abs(x)))
    
    elif len(heap) != 0:
        num, sign = heapq.heappop(heap)
        print(sign * num)
    
    else:
        print(0)