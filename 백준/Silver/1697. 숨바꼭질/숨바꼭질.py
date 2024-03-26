import sys
input = sys.stdin.readline

# 1. 걷기 : x+1 or x-1
# 2. 순간이동 : 2*x
# n -> k 로 가는 가장 빠른 시간

n, k = map(int, input().split())

# bfs 로 q에 넣을 때마다 time 증가

from collections import deque

visited = [0] * 100001
def bfs(x):
    q = deque()
    q.append(x)

    while q:
        a = q.popleft()
        if a == k:
            print(visited[a])
            break
        for i in (a-1, a+1, a*2):
            if 0 <= i <= 100000 and not visited[i]:
                q.append(i)
                visited[i] = visited[a] + 1

bfs(n)