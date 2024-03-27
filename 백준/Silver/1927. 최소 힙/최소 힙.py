import sys
input = sys.stdin.readline

import heapq

# x : 자연수 -> 배열에 x 삽입
# x : 0 -> 가장 작은 값 pop

min_heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)
    else:
        heapq.heappush(min_heap, x)
