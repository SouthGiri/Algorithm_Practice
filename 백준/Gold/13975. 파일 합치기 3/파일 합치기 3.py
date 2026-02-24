import sys
input = sys.stdin.readline

import heapq

def solution(data):
    ans = 0
    heapq.heapify(data)

    while len(data) > 1:
        a = heapq.heappop(data)
        b = heapq.heappop(data)
        res = a+b

        ans += res
        heapq.heappush(data, res)

    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print(solution(data))