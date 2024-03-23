import sys
input = sys.stdin.readline
from collections import deque
# bfs
# 1번부터 시작
q = deque()
def bfs(x):
    visited[x] = True
    q.append(x)
    while q:
        a = q.popleft()
        for i in adj[a]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True


num = int(input())
visited = [0] * (num+1)
adj = [[] * i for i in range(num+1)]

pair = int(input())
for _ in range(pair):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bfs(1)
print(sum(visited) - 1)