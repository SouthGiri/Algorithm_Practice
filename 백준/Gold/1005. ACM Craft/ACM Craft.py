import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    in_deg = [[] for _ in range(N)]
    graph = [[] for _ in range(N)]
    delay = list(map(int, input().split()))
    for _ in range(K):
        X, Y = map(int, input().split())
        in_deg[Y-1].append(X-1)
        graph[X-1].append(Y-1)
    W = int(input())

    ans = [0] * N
    q = deque()

    for idx, node in enumerate(in_deg):
        if len(node) == 0:
            ans[idx] = delay[idx]
            q.append(idx)

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            in_deg[nxt].remove(now)
            if len(in_deg[nxt]) == 0:
                q.append(nxt)

            ans[nxt] = max(ans[nxt], ans[now]+delay[nxt])
            
    print(ans[W-1])