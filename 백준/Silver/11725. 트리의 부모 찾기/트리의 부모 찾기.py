import sys
input = sys.stdin.readline

n = int(input())
vertex_list = [[] for _ in range(n+1)]
res = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    vertex_list[a].append(b)
    vertex_list[b].append(a)

from collections import deque

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for v in vertex_list[now]:
        if res[v] == 0:
            res[v] = now
            q.append(v)

for i in res[2:]:
    print(i)