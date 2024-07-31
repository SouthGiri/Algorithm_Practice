import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def mst(start, weight):
    visit = [0 for _ in range(v+1)]

    q = [[weight, start]]
    ans = 0
    cnt = 0
    while cnt < v:
        w, node = heappop(q)
        if visit[node]: continue
        visit[node] = 1
        ans += w
        cnt += 1
        for dst, weight in graph[node]:
            heappush(q, (weight, dst))
    
    print(ans)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dst, weight = map(int, input().split())
    graph[src].append((dst, weight))
    graph[dst].append((src, weight))

mst(1,0)