import sys
input = sys.stdin.readline

def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n-1:
                    return True
    return False


t = int(input())
for _ in range(t):
    n,m,w = map(int, input().split())
    edges = []
    dist = [1e9] * (n+1)
    for _ in range(m):
        s,e,t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int, input().split())
        edges.append((s,e,-t))

    if not bf():
        print('NO')    
    else:
        print('YES')
