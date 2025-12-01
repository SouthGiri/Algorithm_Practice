from collections import deque

def prt_rank():
    if 0 not in in_deg:
        print('IMPOSSIBLE')
        return
    
    res = []
    q = deque([in_deg.index(0)])
    while q:
        now = q.popleft()
        res.append(now)
        in_deg[now] = -1
        if len(q) != 0:
            print('?')
            return
        
        for nxt in adj[now]:
            in_deg[nxt] -= 1
            
            if in_deg[nxt] == 0:
                q.append(nxt)

    if len(res) != N:
        print('IMPOSSIBLE')
        return
    print(*res[::-1])

def change(src, dst):
    adj[src].remove(dst)
    adj[dst].append(src)
    in_deg[src] += 1
    in_deg[dst] -= 1

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    adj = [[] for _ in range(N+1)]
    in_deg = [0] * (N+1)
    in_deg[0] = -1
    
    for i in range(1, N):
        for j in range(i+1, N+1):        
            adj[data[j-1]].append(data[i-1])
            in_deg[data[i-1]] += 1

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        
        if data.index(a) < data.index(b):
            change(b, a)
        else:
            change(a, b)

    prt_rank()