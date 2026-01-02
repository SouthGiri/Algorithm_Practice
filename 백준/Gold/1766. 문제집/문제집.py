import sys
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_deg = [0] * (N+1)
in_deg[0] = -1
for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    in_deg[dst] += 1

h = []
for problem in range(1, N+1):
    if in_deg[problem] == 0:
        heapq.heappush(h, problem)

while h:
    problem = heapq.heappop(h)
    for nxt in graph[problem]:
        in_deg[nxt] -= 1
        if in_deg[nxt] == 0:
            heapq.heappush(h, nxt)
    print(problem, end=' ')